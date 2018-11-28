import os,sys

def getTime(case):
    case = case.split()
    n = int(case.pop(0))
    ot,bt,te = 0,0,0
    op,bp = 1,1
    for i in range(n):
        rn = case.pop(0)
        kn = int(case.pop(0))
        if(rn == 'O'):
            ot += abs(kn-op)
            if (ot < te): ot = te
            ot+=1
            op = kn
        else:
            bt += abs(kn-bp)
            if (bt < te): bt = te
            bt+=1
            bp = kn
        te =max(ot,bt)
    return te        
            
    

inputFile = open('a-small.in','r')
sys.stdin = inputFile
output = open('a-small.out','w')
t = int(input())
for i in range(t):
    case = input()
    print('Case #' + str(i+1) + ': ' + str(getTime(case)), file = output)
output.close()
inputFile.close()
