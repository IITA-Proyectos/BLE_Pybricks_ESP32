from time import sleep_ms
from bleradio import BLERadio

# A board can broadcast small amounts of data on one channel. Here we broadcast
# on channel 5. This board will listen for other boards on channels 4 and 18.
radio = BLERadio(broadcast_channel=5, observe_channels=[4]) # Aqui podes sumar cuantos canales necesites en la lista!!

# You can run a variant of this script on another board, and have it broadcast
# on channel 4 or 18, for example. This board will then receive it.

counter = 0

from machine import Pin
import time

myLED = Pin(0, Pin.OUT)
myLED_rojo = Pin(48, Pin.OUT)

while True:

    # Data observed on channel 4, as broadcast by another board.
    # It gives None if no data is detected.
    observed = radio.observe(4)
    
    if observed != None and observed[0] <= 50: # Observa el valor del sensor de Distancia
      myLED.value(0)
    else:
      myLED.value(1)
    
    if observed != None and observed[1]: # Observa el valor del sensor de Tacto
      myLED_rojo.value(1)
    else:
      myLED_rojo.value(0)
    print(f"Llego --> {observed}")

    data = ["hello, world!", 3.14, counter]
    # Broadcast some data on our channel, which is 5.
    radio.broadcast(data)
    # print(f"Salio --> {data}")
    counter += 1
    sleep_ms(10)