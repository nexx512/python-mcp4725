MCP4725_ADDR = 0b1100000

class MCP4725:

  def __init__(self, i2c, v_ref, a0 = 0):
    self.i2c = i2c
    if (a0 != 0) and (a0 != 1):
      raise ValueError("Invalid Adress bit: " + a0)
    self.addr = MCP4725_ADDR + a0
    self.v_ref = v_ref

  def v_ref(self):
    return self.v_ref

  def write(self, v):
    value = max(min(int(v / self.v_ref * 4096), 4095), 0)
    msb = (value >> 8) & 0b0001111
    lsb = value & 0b11111111
    self.i2c.writeto(self.addr, bytes([msb, lsb]))
