# Code adapté de :
# https://github.com/itechnofrance/micropython/blob/master/librairies/paj7620/use_paj7620.py
# Utilisation de librairie du capteur de gestes PAJ7620 adaptée disponible sous 
# https://github.com/christianDUCROS/capteur_paj7620/edit/main 
from machine import Pin, SoftI2C
import time
import paj7620

#brochage I2C0
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)

#instanciation capoteur de gestee
g= paj7620.PAJ7620(i2c)

while True:
    # Lecture position joystick
    posx,posy = g.pos_xy()
   
    # Affichage shell position joystick
    print('posx = {}\t posy = {}'.format(posx,posy))   

    # Temporisation de 10 millisecondes
    time.sleep(0.1)
