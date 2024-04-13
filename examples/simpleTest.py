# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
#from machine import Pin, I2C
from bmp581 import bmp581
from smbus_adaption import ByteSMBus

i2c = ByteSMBus(1) # Correct I2C pins for RP2040
bmp = bmp581.BMP581(i2c)

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure

while True:
    print(f"Pressure: {bmp.pressure:.2f}kPa")
    print(f"Temperature: {bmp.temperature:.2f}°C")
    print()
    time.sleep(0.5)

