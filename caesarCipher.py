# caesar cipher encoder and decoder

def decoder(cipher, offset):
  import string
  alphabet = string.ascii_lowercase + string.ascii_lowercase
  decipher = ''
  for letter in cipher.lower():
    if letter in alphabet:
      index = alphabet.find(letter)
      new_index = index+offset
      decipher += alphabet[new_index]
    else:
      decipher += letter
  return decipher
  
def encoder(input_message, offset):
  import string
  alphabet = string.ascii_lowercase
  cipher = ''
  for letter in input_message.lower():
    if letter in alphabet:
      index = alphabet.find(letter)
      new_index = index-offset
      cipher += alphabet[new_index]
    else:
      cipher += letter
  return cipher

# bruteforcer to identify the offset of an encoded message
def bruteforcer(message):
  for offset in range(26):
    print ('Offset:', offset, decoder(message, offset))