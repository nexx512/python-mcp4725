import unittest
from unittest.mock import Mock
from src.mcp4725 import MCP4725

class Fan_Test(unittest.TestCase):

  ADDR = 0b1100001
  REFERENCE_VOLTAGE = 3.3

  def setUp(self):
    self.i2c = Mock()
    self.i2c.writeto = Mock()
    self.mcp4725 = MCP4725(i2c = self.i2c, v_ref = self.REFERENCE_VOLTAGE, a0 = 1)

  def test_set_dac_value_to_zero_for_zero_voltage(self):
    # given

    # when
    self.mcp4725.write(0)

    # then
    self.i2c.writeto.assert_called_with(self.ADDR, b'\x00\x00')

  def test_set_dac_value_to_zero_for_negative_voltage(self):
    # given

    # when
    self.mcp4725.write(-1)

    # then
    self.i2c.writeto.assert_called_with(self.ADDR, b'\x00\x00')

  def test_set_dac_value_according_to_desired_voltage(self):
    # given

    # when
    self.mcp4725.write(2)

    # then
    self.i2c.writeto.assert_called_with(self.ADDR, b'\x09\xb2')

  def test_set_dac_value_to_maximum(self):
    # given

    # when
    self.mcp4725.write(self.REFERENCE_VOLTAGE)

    # then
    self.i2c.writeto.assert_called_with(self.ADDR, b'\x0f\xff')

  def test_set_dac_value_above_maximum(self):
    # given

    # when
    self.mcp4725.write(3.4)

    # then
    self.i2c.writeto.assert_called_with(self.ADDR, b'\x0f\xff')

if __name__ == '__main__':
  unittest.main()
