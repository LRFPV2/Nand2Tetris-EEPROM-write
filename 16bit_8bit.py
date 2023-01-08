from platform import machine


f0 = open('eepromLSB.bin', 'w+b')
f1 = open('eepromMSB.bin', 'w+b')
machine_code = [
    
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000000000000000,
    0b0000011111100110,
    0b1110110000010000,
    0b0000100110011001,
    0b1110001100001000,
    0b0000011111100110,
    0b0000011111100110,
    0b0000011111100110,
    0b0000011111100110,
    0b1110101010000111


]
# LSB
list0 = []
# MSB
list1 = []
mask0 = 0b0000000011111111
for i in range(0, len(machine_code)):
    list0.append(machine_code[i] & mask0)
    list1.append(machine_code[i] >> 8)
print(list0)
print(list1)
byte0 = bytearray(list0)
byte1 = bytearray(list1)
f0.write(byte0)
f1.write(byte1)
f0.close()
f1.close()
