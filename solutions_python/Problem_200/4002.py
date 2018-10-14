def isTidy(number):
    for i in range(len(number) - 1):
        if number[i] > number[i+1]:
            return(False)
    return (True)
def findUntidy(number):
    for i in range(len(number) - 1):
        if number[i] > number[i+1]:
            return(i)

with open('./B-large.in') as fIn:
    fOut = open(fIn.name[:-2]+'out','w')
    next(fIn)
    for i, line in enumerate(fIn):
        sOut = 'Case #' + str(i+1) + ': '

        number = int(line)
        sNumber = str(number)
        while not isTidy(sNumber):
            badIndex = findUntidy(sNumber)
            sNumber = sNumber[0:badIndex] + str(int(sNumber[badIndex]) - 1) + "9" * (len(sNumber) - badIndex - 1)

        while sNumber[0] == "0":
            sNumber = sNumber[1:]
        sResult = sNumber
        sOut = sOut + sResult + '\n'
        fOut.write(sOut)
