import board
import analogio
import digitalio
import time

class MAX471:
    
    def __init__ (
        self, voltage_pin: pin, current_pin: pin
        ) -> None:
        self.voltage = analogio.AnalogIn(voltage_pin)
        self.current = analogio.AnalogIn(current_pin)
    
    def Voltage(self):
        """ Voltage measure  (calibrated) """
        n_result = 0
        for i in range(20):
            n_result += self.voltage.value
            #print(n_result)
            time.sleep(0.1) 
        result =(((n_result * 0.825) / 65535) * 1.0213) - 0.141
        display = ("{:.2f}").format(result)
        self.v_result = result
        return result
    
    def Current(self):
        """ Currrent measure (calibrated)"""
        n_result = 0
        for i in range(20):
            n_result += self.current.value
            #print(n_result)
            time.sleep(0.1) 
        result = (((n_result * 150) / 65535) * 1.0789) - 8.0218
        display = ("{:.2f}").format(result)
        self.c_result = result
        return display
    
    def Power(self):
        """Power = Current * Voltage"""
        result = self.c_result/1000 * self.v_result
        display = ("{:.2f}").format(result)
        return display
"""
max471 = max471(voltage_pin = board.A0, current_pin = board.A1)


while True:
    C = max471.Current()
    V = max471.Voltage()
    P = max471.Power()
"""    

    