import pprint

f = open('C-small-attempt0.in', 'r')
cases = f.readline()
fWrite = open('C-small-attempt0.out', 'w')

for i in range(int(cases)):    
    dataParse = f.readline().split()
    runTimes = int(dataParse[0])
    cartSize = int(dataParse[1])
    groupCount = int(dataParse[2])
    lGroups = f.readline().split()
    income = 0
    currentSpot = 0
    for k in range(runTimes):
        currentLoad = 0
        bContinue = True
        count = 0
        while( currentLoad + int(lGroups[currentSpot % int(groupCount)]) <= cartSize):
           if count == int(groupCount):
               break
           else:
               income = income + int(lGroups[currentSpot % int(groupCount)])
               currentLoad = currentLoad + int(lGroups[currentSpot % int(groupCount)])
               currentSpot = currentSpot + 1
               count = count + 1
    strOut = "Case #"+str(i+1)+': '+str(income)+'\n'
    fWrite.write(strOut);
    print strOut

f.close()
fWrite.close()
