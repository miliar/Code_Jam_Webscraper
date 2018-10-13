myfile = open("D-large.in.txt", "r")
output = open("output.txt", "w")
import math
cases = int(myfile.readline().strip())
case = 0

while case < cases:
    
    blockNum = int(myfile.readline().strip())
    naomi = myfile.readline().split()
    ken = myfile.readline().split()
    
    naomi.sort()
    ken.sort()

    war = 0
    deceitfulWar = 0
    count = 1
    dCountKenHighest = blockNum-1
    dCountKenLowest = 0
    dCountNaomiLowest = 0
    dCountNaomiHighest = blockNum-1
    
    wKenHigh = blockNum -1
    wKenLow = 0
    wNaomiHigh = blockNum -1
    wNaomiLow = 0
    

    while count <= blockNum:
        if float(naomi[dCountNaomiHighest]) > float(ken[dCountKenHighest]):
            deceitfulWar += 1
            dCountNaomiHighest -= 1
            dCountKenHighest -= 1
 
        else:
            dCountNaomiLowest += 1
            dCountKenHighest -= 1
        if float(naomi[wNaomiHigh]) > float(ken[wKenHigh]):
            war +=1
            wNaomiHigh -=1
            wKenLow += 1
        else:
            wKenHigh -=1
            wNaomiHigh -=1
        count +=1
 
    output.write("Case #"+ str(case+1) + ": " + str(deceitfulWar) + " " + str(war)+ "\n")
    case += 1

myfile.close()
output.close()

