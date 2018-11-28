#
# problemA.py
#

# Import
import sys
sys.dont_write_bytecode = True
sys.path.append('../')
from gcj import Problem
from gcj.utils import Timer

class Horse():

    def __init__(self,K,S):
        self.K = float(K)
        self.S = float(S)

# Parser
def parser(fin):
    [D,N] = fin.readInts()
    H = []
    for _ in xrange(N):
        K,S = fin.readInts()
        H.append((K,S))
    
    return D,N,H

def solver(data):
    D,N,H = data

    H = sorted(H)[::-1]

    H = [Horse(h[0],h[1]) for h in H]

    for h in H:
        print h.K,h.S

    T = []
    T.append((D-H[0].K)/H[0].S)

    for i in xrange(1,len(H)):
        if H[i].S <= H[i-1].S:
            T.append((D-H[i].K)/H[i].S)
        else:
            # Collision at
            print 'Collision'
            t = (H[i-1].K-H[i].K)/(H[i].S-H[i-1].S)
            k = H[i].S*t+H[i].K
            print t,k

            if k >= D:
                T.append((D-H[i].K)/H[i].S)
            else:
                T.append(T[-1])

    print T

    return '{0:.6f}'.format(D/T[-1])


# Main
if __name__ == '__main__':
    with Timer('Problem A'):
        Problem(parser, solver).run()
