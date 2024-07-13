#!/usr/bin/python3

from Crypto.Cipher import AES

# my device uid '10063F1FB910E0DC'
uid = b'10063f1f'
#uid = b'10093f30'
# AES key "59494F4754fff00" store in firmware
key = b'59494F4754fff00\0'

aes = AES.new(key, AES.MODE_ECB)

dat = aes.encrypt(uid + uid)

print(dat[:8].hex().encode('ascii').hex())

# calc the result
# '37 39 37 36 39 32 62 39 35 63 39 61 63 64 34 34'
# '37393736393262393563396163643434'
