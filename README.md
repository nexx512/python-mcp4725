# MCP4725 Driver

Driver for the MCP4725 DAC converter using a micropython I²C interface.

## Dependencies

None

## Usage

Create a micropython I2C Object and pass it to the constructor.
Create an MCP4725 instance providing the reference voltage.
Write a voltage using `MCP4725.write(v)`.

```python
from machine import Pin, I2C, Timer
from mcp4725 import MCP4725

i2c = i2c_0 = I2C(1, scl = Pin(11), sda = Pin(10), freq = 400000)
mcp4725 = MCP4725(i2c = i2c, v_ref = 3.3)
mcp4725.write(v = 2.2)
```

## Test

```
$ python3 -m unittest discover
```
