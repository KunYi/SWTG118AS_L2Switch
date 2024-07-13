#!/usr/bin/python3

from Crypto.Cipher import AES
import binascii

def get_uid(uid_string):
    """
    Convert the UID string to lowercase and then to a byte array of specified length.

    Parameters:
    uid_string (str): The UID string to be converted.

    Returns:
    bytes: The converted byte array.
    """
    # Convert the string to lowercase
    lowercase_uid = uid_string.lower()

    # Take the required number of characters
    suid = lowercase_uid[:8]

    # Convert the shortened string to a byte array
    ba_uid = suid.encode('ascii')
    print('uid:', ba_uid)

    return ba_uid

# my device uid '10063F1FB910E0DC'
uid = get_uid('10063F1FB910E0DC')

# AES key "59494F4754fff00" store in firmware
key = b'59494F4754fff00\0'

aes = AES.new(key, AES.MODE_ECB)

dat = aes.encrypt(uid + uid)

hex_otp = dat[:8].hex().encode('ascii').hex()
print('otp hex:', hex_otp)

otp = binascii.unhexlify(hex_otp)
print('otp:', otp)

buff = bytearray([0xFF] * 1024)
buff[0:16] = otp
buff[256:256+15] = otp[1:]
buff[512:512+14] = otp[2:]
buff[768:768+13] = otp[3:]

with open('otp.bin', 'wb') as f:
    f.write(buff)
print("Binary data written to otp.bin")

