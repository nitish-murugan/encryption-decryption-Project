import csv
import random
import time as t
boolean = 1
while(boolean):
    choice = int(input("\nPress 1 => Encrypting \nPress 2 => Decrypting \nPress 3 => Exit \nEnter your choice => "))
    if(choice == 1):
        numbers = []
        alphabets = []
        encrypt = ""
        for i in range(66):
            num = random.randint(1000,9999)
            num = str(num)
            if(num not in numbers):
                numbers.append(num)
            else:
                num = random.randint(1000,9999)
                num = str(num)
                if(num not in numbers):
                    numbers.append(num)
                else:
                    num = random.randint(1000,9999)
                    num = str(num)
                    if(num not in numbers):
                        numbers.append(num)
        for i in range(97,123):
            character = chr(i)
            alphabets.append(character)
        for i in range(65,91):
            character = chr(i)
            alphabets.append(character)
        alphabets.append(chr(32))
        alphabets.append(chr(44))
        alphabets.append(chr(46))
        alphabets.append(chr(34))
        for r in range(10):
            alphabets.append(str(r))
        #print(alphabets)
        txt = input("Please enter the text : ")
        for i in txt:
            index = 0
            for j in alphabets:
                if(i == j):
                    encrypt+=numbers[index]
                else:
                    index+=1
        location ="Encrypt.csv"
        
        with open("Encrypt.csv","w") as fileObject:
            writer = csv.writer(fileObject)
            writer.writerow(numbers)
            writer.writerow(alphabets)
            writer.writerow(encrypt)
            print("Algorithm and patters file is successfully saved in the location => ",location)
        fileObject.close()
        print("Encrypted text is => ",encrypt)
                #Decrypting
    elif(choice == 2):
        print("Please store the encryption details in the file named Encrypt.csv as per the software rules")
        ii = input("Please hit enter button as soon as encryption details are uploaded in the file")
        print("The decrypted text is")
        fileObject = open("Encrypt.csv","r")
        reader_1 = csv.reader(fileObject)    #array[0] => random numbers
                                             #array[2] => alphabets
                                             #array[4] => encrypt txt
        reader = list(reader_1)
        randomNumber = reader[0]
        randomAlphabet = reader[2]
        encryptTxt = reader[4]
        newEncryptTxt = ""
        decryptTxt = ""
        loops = int(len(encryptTxt)/4)
        a = 0
        for i in range(1,loops+1):
            for j in range(4):
                newEncryptTxt +=encryptTxt[a]
                a+=1
            a = 4*i
            index = 0
            for k in randomNumber:
                if(newEncryptTxt == k):
                    print(randomAlphabet[index],end="")
                    decryptTxt += randomAlphabet[index]
                    break
                else:
                    index+=1
            newEncryptTxt = ""
        #print(decryptTxt)
        print("\n")
    elif(choice == 3):
        break
    else:
        print("Enter the right choice")
