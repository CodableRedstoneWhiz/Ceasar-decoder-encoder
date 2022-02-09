

def encrypt(key, message):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  message  = message.upper()
  result = ""
  key = key
  for i in message:
    for z in range(len(alpha)):
      if i == alpha[z]:
        result = result + alpha[(z + key) % len(alpha)]
  print(result + "\n")

def decrypt(key, message):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  message  = message.upper()
  result = ""
  for letter in message:
    if letter in alpha:
      letter_index = (alpha.find(letter) - key) % len(alpha)

      result = result + alpha[letter_index]

  print(result + "\n")

def decryptWithoutKey(message):
  message = message.upper()
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  for i in range(len(alpha)):
    print("Key:" + str(i))
    decrypt(i, message)
    print("\n")
    #print(decrypt(i, message))

#decrypt(3, "khoor")
def bootup():
  EorDorQ = input("Do you want to Encrypt (E) Decrypt (D) or quit (Q)? \n")
  if isinstance(EorDorQ, str):
    EorDorQ = EorDorQ.upper()
  else: 
    print("please input either E, D, or Q. Please restart the program")

  if EorDorQ == "E":
    message = input("Please input the message you want to encrypt \n").upper()
    key = int(input("Please enter the amount of offset you want \n"))
    encrypt(key, message)
    bootup()

  if EorDorQ == "D":
    message = input("Please input the message you want to decrypt \n").upper()
    decryptWithoutKey(message)
    bootup()

  if EorDorQ == "Q":
    print("bye bye")

  

#findKey("khoor")

bootup()
