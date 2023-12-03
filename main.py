import machine # import the machine module
import utime # import the utime module

led = machine.Pin(25, machine.Pin.OUT) # create a Pin object for the onboard LED
led(1)
utime.sleep(2)
led(0)

sensor_temp = machine.ADC(4) # create an ADC object on pin 4
conversion_factor = 3.3 / (65535) # calculate the conversion factor

while True: # loop forever
    reading = sensor_temp.read_u16() * conversion_factor # read the sensor value and convert it to voltage
    temperature = 27 - (reading - 0.706)/0.001721 # calculate the temperature from the voltage
    
    utime.sleep(1) # wait for 0.5 seconds
    if 0.00 <= temperature <= 19.00:
        led.value(0)
        led.value(0)
        
    if 20.00 <= temperature <= 25.00:
        led.value(0)
        led.value(1)
        
    if 26.00 <= temperature <= 30.20:
        led.value(1)
        utime.sleep(1)
        led.value(0)
        utime.sleep(1)
        led.value(1)
        
    if temperature < 3.00:
        print('im cold')
    print( temperature, "°C") # print the temperature in Celsius