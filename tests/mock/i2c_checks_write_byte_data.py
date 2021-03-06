#!/usr/bin/env python

# Author: Alex Tereschenko <alext.mkrs@gmail.com>
# Copyright (c) 2016 Alex Tereschenko.
#
# SPDX-License-Identifier: MIT

import mraa as m
import unittest as u

from i2c_checks_shared import *

class I2cChecksWriteByteData(u.TestCase):
  def setUp(self):
    self.i2c = m.I2c(MRAA_I2C_BUS_NUM)

  def tearDown(self):
    del self.i2c

  def test_i2c_write_byte_data(self):
    self.i2c.address(MRAA_MOCK_I2C_ADDR)
    test_byte = 0xEE
    reg = MRAA_MOCK_I2C_DATA_LEN - 1
    self.assertEqual(self.i2c.writeReg(reg, test_byte),
                     m.SUCCESS,
                     "I2C writeReg() did not return success")
    self.assertEqual(self.i2c.readReg(reg),
                     test_byte,
                     "I2C readReg() after writeReg() returned unexpected data")

  def test_i2c_write_byte_data_invalid_addr(self):
    self.i2c.address(MRAA_MOCK_I2C_ADDR - 1)
    test_byte = 0xEE
    reg = MRAA_MOCK_I2C_DATA_LEN - 1
    self.assertEqual(self.i2c.writeReg(reg, test_byte),
                     m.ERROR_UNSPECIFIED,
                     "I2C writeReg() to invalid address did not return error")

  def test_i2c_write_byte_data_invalid_reg(self):
    self.i2c.address(MRAA_MOCK_I2C_ADDR)
    test_byte = 0xEE
    reg = MRAA_MOCK_I2C_DATA_LEN
    self.assertEqual(self.i2c.writeReg(reg, test_byte),
                     m.ERROR_UNSPECIFIED,
                     "I2C writeReg() with invalid register did not return error")

if __name__ == "__main__":
  u.main()
