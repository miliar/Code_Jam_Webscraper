#shyness google code jam

def giveStandingOvation(Smax, shy):
    totOva = 0
    addFrnds = 0
    for i in range(Smax + 1):
        if totOva >= i:
            totOva += shy[i]
        elif shy[i] != 0:
            addFrnds += (i - totOva)
            totOva += (i - totOva + shy[i]) 
    return addFrnds    

inPath = 'I:\googleCodeJam\A-large.in'
outPath = 'I:\googleCodeJam\A-large.out'
inContent = open(inPath, 'r')
outContent = open(outPath, 'w')
testCases = int(inContent.readline())

for i in range(testCases):
    input1 = inContent.readline()
    input1List = input1.split()
    Smax = int(input1List[0])
    shy = [int(c) for c in input1List[1]]  
    
    outContent.write('Case #%d: %d'%(i+1,giveStandingOvation(Smax, shy))+'\r\r\n')

inContent.close()        
outContent.close()