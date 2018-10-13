INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'tidy_numbers.o'

outputFile = open(OUTPUT_FILE,'w+')

def isTidy(num):
    for i in range(len(num)-1):
        if(int(num[i]) > int(num[i+1])):
            return False
    return True

def getBiggestNumPos(num):
    biggestnumber = int(num[0])
    for i in range(1,len(num)):
        if(biggestnumber < int(num[i])):
            biggestnumber = int(num[i])
    return num.find(str(biggestnumber))

def tidyNumbers(inp,caseNum):
    if(int(inp) < 10):
        outputFile.write('Case #'+str(caseNum)+': ' + str(inp) + '\n')
        return
    inp_length = len(inp)
    while(isTidy(inp) == False):
        biggestNumPos = getBiggestNumPos(inp)
        #secondBiggestNumPos = getBiggestNumPos(inp[:biggestNumPos] + '0' + inp[biggestNumPos+1:])
        inp = inp[:biggestNumPos] + str(int(inp[biggestNumPos])-1)
        for x in range(inp_length - len(inp)):
            inp += '9'
    outputFile.write('Case #'+str(caseNum)+': ' + str(int(inp)) + '\n')
    return

def getInputs():
    inpFile = open(INPUT_FILE,'r')
    inputs = inpFile.read().splitlines()
    inpFile.close()
    inputs.pop(0)
    return inputs

pos=1
inputs = getInputs()
for inp in inputs:
    tidyNumbers(inp,pos)
    pos=pos+1
outputFile.close()