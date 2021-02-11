
import pyvisa as py

# write you own address here
address_2182a = 'GPIB0::01::INSTR'
address_2440 = 'GPIB0::02::INSTR'
address_6221 = 'GPIB0::03::INSTR'

class keithley_2182a:

    def __init__(self):
        rm = py.ResourceManager()
        self.equ_2182a = rm.open_resource(address_2182a)
        #  set up here 
        self.equ_2182a.write("*rst")
        self.equ_2182a.write(":sens:chan 1")
        self.equ_2182a.write(":sens:func 'VOLT'")

    def record(self):
        reading = float(self.equ_2182a.query("read?"))
        return reading
    
class keithley_2440:
    def __init__(self):
        rm = py.ResourceManager()
        self.equ_2440 = rm.open_resource(address_2440)
        self.equ_2440.write("*rst")
        self.equ_2440.write(":sour:func curr")
        self.equ_2440.write(":sour:curr:mode fix")

    def set_compliance(self,compliance):
        self.equ_2440.write(":sens:curr:prot {}".format(compliance))
    
    def reset(self):
        self.equ_2440.write("*rst")
        self.equ_2440.write(":sour:func curr")
        self.equ_2440.write(":sour:curr:mode fix")

    def set_current(self, current):
        self.equ_2440.write(":sour:curr:level {}".format(current))

    def output(self, option):
        if (option):
            self.equ_2440.write("outp on")
        else :
            self.equ_2440.write("outp off")

class keithley_6221:
    def __init__(self):
        
        rm = py.ResourceManager()
        self.equ_6221 = rm.open_resource(address_6221)
        
    def reset(self):
        self.equ_6221.write("*rst")

    def auto_range(self,option):
        if (option):
            self.equ_6221.write("curr:rang:auto on")
        else :
            self.equ_6221.write("curr:rang:auto  off")

    def set_compliance(self,compliance):
        self.equ_6221.write("curr:comp {}".format(compliance))

    def set_current(self,current):
        self.equ_6221.write("curr %f" % current)

    def output(self,option):
        if (option):
            self.equ_6221.write("outp on")
        else :
            self.equ_6221.write("outp off")

    def wave_sin(self,amplitude, frequency, offset):
        self.equ_6221.write("sour:wave:func sin")
        self.equ_6221.write("sour:wave:ampl {}".format(amplitude))
        self.equ_6221.write("sour:wave:freq {}".format(frequency))
        self.equ_6221.write("sour:wave:offs {}".format(offset))

    def phase_maker(self,option):
        if(option):
            self.equ_6221.write("sour:wave:pmar:stat on")
        else:
            self.equ_6221.write("sour:wave:pmar:stat off")

    def set_phase_maker(self, degree):
        self.equ_6221.write("sour:wave:pmark {}".format(degree))

    def wave_range(self,option):
        if (option == 'fix'):
            self.equ_6221.write("sour:wave:rang fix")
        else :
            self.equ_6221.write("sour:wave:rang best")

    def set_offset(self, offset):
        self.equ_6221.write("sour:wave:offs {}".format(offset))
        
    def set_wave_duration(self,t):
        self.equ_6221.write("sour:wave:dur:time {}".format(t))

    def set_wave_amp(self,amplitude):
        self.equ_6221.write("sour:wave:ampl {}".format(amplitude))

    def set_wave_fre(self,frequency):
        self.equ_6221.write("sour:wave:freq {}".format(frequency))

    def arm_wave(self):
        self.equ_6221.write("SOUR:WAVE:ARM")

    def wave_init(self):
        self.equ_6221.write("SOUR:WAVE:INIT")

    def wave_abort(self):
        self.equ_6221.write("sour:wave:abor")
