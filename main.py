import machine
from lib.lorawan import LoRaWAN
from lib.config import Keys
'''
Example sending the value 10 in hex(0A) every 60 seconds
'''

lora = LoRaWAN(Keys['DevEUI'], Keys['AppEUI'], Keys['AppKey'])
#lora.reset() # uncomment to reset RAK811 and rejoin
if not lora.has_joined:
    while not lora.has_joined:
        lora.join()
    print('Network joined')

print('Network ready')

lora.send('0A')

machine.deepsleep(60 * 1000)
