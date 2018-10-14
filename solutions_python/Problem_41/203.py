import os
import math

os.chdir(os.getcwd())
caseLine = ""
fin = open("B-small-attempt3.in", "r")
lines = fin.readlines();
fin.close()

numOfCases = int(lines[0])

for i in range(1, numOfCases+1):

    number = lines[i]
    
    
    digs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    digs2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(0, len(number)-1):
        
        if number[j] != '0':
            digs[int(number[j])] += 1

    num = int(number)

    found = False
    count = 0
    numofnums = 0
    print(num)
    for j in range(0, len(digs)):
        if digs[j] == 1:
            count += 1
        if digs[j] >= 1:
            numofnums += 1

    if count == 1 and numofnums == 1:
        print(num)
        found = True
            

    if found == True:
        num = str(num)
        num += "0"
    

    while found == False:
        num = int(num)
        num += 1
        num = str(num)
        found = True
        digs2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for h in range(0, len(str(num))):
            #print(num[h])
            if num[h] != '0':
                digs2[int(num[h])] = digs2[int(num[h])] + 1

        #print (digs, "digs")
        #print(digs2, "digs2")
        for a in range(0, len(digs)):
            if digs[a] != digs2[a]:
                found = False
                break

    caseLine = caseLine + "Case #" + str(i) + ": " + str(num) + "\n"
    #print("ok")
  
fout = open("outsmall2.txt", "w")
fout.write(caseLine)
fout.close()
                
        
            

    
