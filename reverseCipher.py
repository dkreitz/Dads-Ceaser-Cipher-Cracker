# Reverse Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

message = 'Three can keep a secret, if two of them are dead.'
message1 = '.daed era meht fo owt fi ,terces a peek nac eerhT'
translated = ''

i = len(message) - 1
while i >= 0:
  translated = translated + message[i]
  i = i - 1

print(translated)
