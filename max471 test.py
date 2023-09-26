import board
import busio
import digitalio
import time
import MAX471

meter = MAX471.MAX471(voltage_pin = board.A0, current_pin = board.A1)
#voltage = analogio.AnalogIn(board.A0)
while True:
    voltage = meter.Voltage()
    print (("{} V").format(voltage))
    #current = meter.Current()
    #print (("{} mA").format(current))
    #power = meter.Power()
    #print(("{} W").format(power))
    time.sleep (0.1)