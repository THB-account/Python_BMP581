import smbus2

class ByteSMBus(smbus2.SMBus):
  def read_i2c_block_data(self,i2c_adrr,register,length,force=None):
    return bytes(smbus2.SMBus.read_i2c_block_data(i2c_addr,register,length,force))
