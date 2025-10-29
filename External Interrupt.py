import machine
import time

def Button_INT(pin):
    if(button.value() == 0):
        time.sleep(0.5)
        led.toggle()
    button.irq(handler=Button_INT)
        
led = machine.Pin("LED",machine.Pin.OUT)
button = machine.Pin(16,machine.Pin.IN,machine.Pin.PULL_UP)
button.irq(trigger=machine.Pin.IRQ_FALLING,handler=Button_INT)

while(True):
    pass