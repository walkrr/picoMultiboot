Pin Mappings: 
* RPi Pico `21` (`SPI0 RX`) pin <-> GBA `SO` pin
* RPi Pico `23` (`GND`) pin <-> GBA `GND` pin
* RPi Pico `24` (`SPI0 SCK`) pin <-> GBA `SC` pin
* RPi Pico `25` (`SPI0 TX`) pin <-> GBA `SI` pin

Before building first use the python script to convert your rom to a hpp file. Due to memory limitations of both
the gba and the pico, only roms up to 256kb can be used. 

Built using the pico multiboot library found in [here](https://github.com/copyrat90/gba-pico-gamepad)
