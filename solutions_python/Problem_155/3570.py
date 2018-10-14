def standingOvation(maxShyness, audienceBinary):
    inputAudienceBinary = audienceBinary
    outputAudienceBinary = audienceBinary
    for p in range(1,maxShyness + 1):
        subProblemAddditionalAudience = standingOvationSubSolver(p, outputAudienceBinary[:p+1])
        if(subProblemAddditionalAudience > 0):
            outputAudienceBinary = addAudienceToIndex1(outputAudienceBinary, subProblemAddditionalAudience)
    #print inputAudienceBinary, "->", outputAudienceBinary
    return int(outputAudienceBinary[0]) - int(inputAudienceBinary[0])

def standingOvationSubSolver(maxShyness, audienceBinary):
    if(maxShyness == 0):
        return audienceBinary
    else :     
        audienceBinary = audienceBinary[:-1]
        result = maxShyness - sumDigit(audienceBinary) 
        if(result > 0):
            return result
        else:
            return 0
            
def addAudienceToIndex1(s, num):
    s = list(s)
    s[0] = str(int(s[0]) + int(num))
    s = "".join(s)
    return s

def sumDigit(s):
    return sum(int(digit) for digit in str(s))

infile = open("A-small-attempt1.in","r")
#infile = open("test.in","r")
l = infile.readline()
l = l.split()
N  = int(l[0])

for i in range(0,N):
    temp = []
    l = infile.readline()
    l = l.split()
    k = int(l[0])
    sa = l[1]
    result = standingOvation(k, sa)
    s = "Case #" + str(i+1) + ":"
    print s, result
    
    #print s, result
    
