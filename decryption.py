import pandas as pd 

def encryptString(plainText, key):
    
    decryptedLenth = len(plainText)
    roundes = decryptedLenth // key
    reminders = decryptedLenth % key

    for i in range(roundes):
        for j in range(i, decryptedLenth, roundes + 1):
            print(plainText[j])

    i = i + 1
    for j in range(i, decryptedLenth, roundes + 1):
        print(plainText[j])

encryptString("hlowrdel ol", 2) 
