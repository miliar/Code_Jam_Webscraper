
def convertListToNumber(NList):
    s = map(str, NList)
    s = ''.join(s)
    s = int(s)
    return s

with open('inB.txt','r') as inFileB, open('outB.txt', 'w') as outFileB:
    caseNum = 0
    for line in inFileB:
        if (caseNum == 0):    # handle the first line
           T = int(line)
           caseNum += 1
        else: # handle cases
            N = int(line)
            NList = [int(x) for x in str(N)]

            for i in range (len(NList)-1):
               if (NList[i]-NList[i+1] > 0):
                   iszero=1
                   index = i
                   if(i>0):
                       iszero = NList[index] - NList[index-1] #check if the last digit equal
                   while ( iszero == 0):
                       index -=1
                       iszero = NList[index] - NList[index - 1]  # check if the last digit equal

                   NList[index] -= 1
                   for j in range(index+1,len(NList)):
                       NList[j] = 9
            tinyN = convertListToNumber(NList)
            outFileB.write('Case #' + str(caseNum) +': ' + str(tinyN) +'\n')
            caseNum += 1


