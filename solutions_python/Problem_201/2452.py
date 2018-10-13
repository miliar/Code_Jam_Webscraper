#
# problemC.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

def LS(stals,s):
    for i in xrange(s-1,-1,-1):
        if stals[i]:
            return s - i - 1
        
def RS(stals,s):
    for i in xrange(s+1,len(stals)):
        if stals[i]:
            return i - s - 1
            

# Parser
def parser(fin):
    return fin.readInts()


# Solver
def solver(data):
    N,K = data
    stals = [0]*(N+2)
    stals[0] = 1
    stals[-1] = 1
    for _ in xrange(K):
        #print 'stals:',stals
        lS = []
        rS = []
        iS = []
              
        for s in [i for i,stal in enumerate(stals) if not stal]:
            iS.append(s)
            lS.append(LS(stals,s))
            rS.append(RS(stals,s))
        minLSRS = [min(lS[i],rS[i]) for i in xrange(len(iS))]
        maxLSRS = [max(lS[i],rS[i]) for i in xrange(len(iS))]
        minLSRSVal = max(minLSRS)
        i = minLSRS.index(minLSRSVal)
        if minLSRS.count(minLSRSVal) > 0:
            for j in xrange(len(iS)):
                if minLSRS[j] == minLSRSVal:
                    if maxLSRS[j] > maxLSRS[i]:
                        i = j
            
        stals[iS[i]] = 1

#    print stals
#    print lS,rS

    ans = '{0} {1}'.format(max(lS[i],rS[i]),min(lS[i],rS[i]))
    print ans
    return ans
          
        
            


# Main
if __name__ == '__main__':
    with Timer('Problem C'):
        Problem(parser, solver).run()
