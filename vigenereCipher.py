# vigenere cipher encoder and decoder

def vigenere_decoder(cipher, keyword):
  import string
  alphabet = string.ascii_lowercase + string.ascii_lowercase
  cipher = cipher.lower()
  key_phrase = ''
  decipher = ''
  index = 0
  for letter in cipher:
    if letter in alphabet:
      key_phrase += keyword[index]
      index += 1
      if index == len(keyword):
        index = 0
    else:
      key_phrase += letter
  indexes = []
  for i in range(len(cipher)):
    if cipher[i] in alphabet:
      cip_val = alphabet.find(cipher[i])
      key_val = alphabet.find(key_phrase[i])
      diff = cip_val + key_val
      indexes.append(diff)
    else:
      indexes.append(cipher[i])
  for item in indexes:
    if type(item) == int:
      decipher += alphabet[item]
    else:
      decipher += item
  return decipher


def vigenere_encoder(cipher, keyword):
  import string
  alphabet = string.ascii_lowercase + string.ascii_lowercase
  cipher = cipher.lower()
  key_phrase = ''
  decipher = ''
  index = 0
  for letter in cipher:
    if letter in alphabet:
      key_phrase += keyword[index]
      index += 1
      if index == len(keyword):
        index = 0
    else:
      key_phrase += letter
  indexes = []
  for i in range(len(cipher)):
    if cipher[i] in alphabet:
      key_val = alphabet.find(key_phrase[i])
      cip_val = alphabet[key_val:].find(cipher[i])
      indexes.append(cip_val)
    else:
      indexes.append(cipher[i])
  for item in indexes:
    if type(item) == int:
      decipher += alphabet[item]
    else:
      decipher += item
  return decipher