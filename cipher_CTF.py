mport wordlist
from secretpy import Vigenere

"""
generators Wordlists 
"""
def generators():
      generator = wordlist.Generator('abcdefghijklmnopqrstuvwxyz')
      return generator


"""
   The Vigenère cipher (French pronunciation:  [viʒnɛːʁ]) is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers, based on the letters of a keyword. It employs a form of polyalphabetic substitution
   First described by Giovan Battista Bellaso in 1553,
   the cipher is easy to understand and implement,
   but it resisted all attempts to break it until 1863,three centuries later.
   This earned it the description le chiffre indéchiffrable (French for 'the indecipherable cipher'). Many people have tried to implement encryption schemes that are essentially Vigenère ciphers.[3] In 1863,
   Friedrich Kasiski was the first to publish a general method of deciphering Vigenère ciphers
   
"""
def VigenereCipher(cipher_v,flags):
     cipher = Vigenere()
     wordlist = generators()
     for each in wordlist.generate(1, 26):
           decrypt = cipher.decrypt(cipher_v,each)
           print(f"Wordlist: {decrypt} : {each} ",end="\r")
           if decrypt in flags:
              print("    -->>> {decrypt} : Key {each} ")
              break
VigenereCipher("hflmocrp","hellobro")
