import pyvisa as py
import time 

class keithley_6221:
    def __init__(self,address_6221):
        
        rm = py.ResourceManager()
        self.equ_6221 = rm.open_resource(address_6221)
        
    def reset(self):
        self.equ_6221.write("*rst")

    def rs_232_2182_read(self):
        self.equ_6221.query('SYST:COMM:SER:ENT?')
        time.sleep(0.1)
        self.equ_6221.write('SYST:COMM:SER:SEND ":sens:data:fresh?"')
        time.sleep(0.1)
        return float(self.equ_6221.query('SYST:COMM:SER:ENT?'))


    def auto_range(self,option):
        if (option):
            self.equ_6221.write("curr:rang:auto on")
        else :
            self.equ_6221.write("curr:rang:auto off")

    def set_compliance(self,compliance):
        self.equ_6221.write(f"curr:comp {compliance}")

    def set_current(self,current):
        self.equ_6221.write(f"curr {current}")
    
    def single_pulse_mode(self,pulse,widt = 500e-6, sdel = 100e-4,point = 2):
        self.equ_6221.write("sour:pdel:rang best")
        self.equ_6221.write(f"sour:pdel:high {pulse}")
        self.equ_6221.write(f"sour:pdel:widt {widt}")
        self.equ_6221.write(f"sour:pdel:sdel {sdel}")
        self.equ_6221.write(f"sour:pdel:coun {point}")
        self.equ_6221.write(f"trac:poin {point}")
    
    # def single_pulse_data(self):
    #     self.result = self.equ_6221.query("Trac:DATA?")
    #     info = self.result.split(",")
    #     return info[0]

    def custom_pulse_mode(self):
        self.equ_6221.write("sour:pdel:swe on")
        self.equ_6221.write("sour:swe:spac list")
    
    def custom_pulse_data(self, data):
        self.equ_6221.write(f"sour:list:curr {data}")

    def custom_pulse_data_append(self,data):
        self.equ_6221.write(f"sour:list:curr:app {data}")
    
    def custom_pulse_delay(self, data):
        self.equ_6221.write(f"sour:list:del {data}")

    def custom_pulse_delay_append(self,data):
        self.equ_6221.write(f"sour:list:del:app {data}")

    def pulse_setting(self, widt = 1000e-6, sdel = 500e-6,point = 10000,loop = 1):
        self.equ_6221.write(f"sour:pdel:lme {2}") # low measuring point
        self.equ_6221.write(f"sour:swe:coun {loop}") # looping time
        self.equ_6221.write(f"sour:pdel:widt {widt}")
        self.equ_6221.write(f"sour:pdel:sdel {sdel}")
        self.equ_6221.write(f"sour:pdel:coun {point}")
        self.equ_6221.write(f"trac:poin {point}")

    def arm_pulse(self):
        self.equ_6221.write("sour:pdel:arm")
    
    def init_pulse(self):
        self.equ_6221.write("init:imm")
    
    def pulse_end(self):
        self.equ_6221.write("sour:swe:abor")
    
    def pulse_data(self):
        result = self.equ_6221.query("Trac:DATA?")
        info = result.split(",")
        information = info[::2]
        return information

    def output(self,option):
        if (option):
            self.equ_6221.write("outp on")
        else :
            self.equ_6221.write("outp off")

    def wave_sin(self,amplitude=None, frequency=None, offset=0):
        self.equ_6221.write("sour:wave:func sin")
        self.equ_6221.write(f"sour:wave:ampl {amplitude}")
        self.equ_6221.write(f"sour:wave:freq {frequency}")
        self.equ_6221.write(f"sour:wave:offs {offset}")

    def phase_maker(self,option):
        if(option):
            self.equ_6221.write("sour:wave:pmar:stat on")
        else:
            self.equ_6221.write("sour:wave:pmar:stat off")

    def set_phase_maker(self, degree):
        self.equ_6221.write(f"sour:wave:pmark {degree}")

    def wave_range(self,option):
        if (option == 'fix'):
            self.equ_6221.write("sour:wave:rang fix")
        else :
            self.equ_6221.write("sour:wave:rang best")

    def set_offset(self, offset):
        self.equ_6221.write(f"sour:wave:offs {offset}")
        
    def set_wave_duration(self,t):
        self.equ_6221.write(f"sour:wave:dur:time {t}")

    def set_wave_amp(self,amplitude):
        self.equ_6221.write(f"sour:wave:ampl {amplitude}")

    def set_wave_fre(self,frequency):
        self.equ_6221.write(f"sour:wave:freq {frequency}")

    def arm_wave(self):
        self.equ_6221.write("SOUR:WAVE:ARM")

    def wave_init(self):
        self.equ_6221.write("SOUR:WAVE:INIT")

    def wave_abort(self):
        self.equ_6221.write("sour:wave:abor")
