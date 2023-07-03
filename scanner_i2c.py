#Scanner I2C 
from machine import Pin, SoftI2C

#brochage I2C0
i2c = SoftI2C(scl=Pin(5), sda=Pin(4), freq=400000)

#affichage de l'adresse
print("I2C Adresse : "+hex(i2c.scan()[0]))
