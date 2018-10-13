import sys
import re
import os
import time
from StringIO import StringIO
from itertools import *
from multiprocessing import Pool
from pprint import pprint

parallel = False

def read(caseNo):
    P = int(next(fin))
    M = [map(int, next(fin).split()) for i in range(P+1)]
    for i in range(P+1):
        assert len(M[i]) == 1<<(P-i)
    return locals()

def solve(data):
    print 'Case #{0}'.format(data.caseNo)

    P = data.P
    M = data.M

    inf = sum(sum(row) for row in M)+100

    c = {}

    for i in range(1<<P):
        for j in range(P+1):
            if j >= P-M[0][i]:
                c[0, i, j] = 0
            else:
                c[0, i, j] = inf

    for round in range(P):
        for i in range(1<<(P-1-round)):
            for j in range(P-round):
                c[round+1, i, j] = min(\
                    M[round+1][i] + c[round, 2*i, j+1] + c[round, 2*i+1, j+1],
                    c[round, 2*i, j] + c[round, 2*i+1, j])
#    pprint(M)
#    pprint(c)                    

    out = StringIO()
    assert c[P, 0, 0] < inf
    print>>out, c[P, 0, 0]
    return out.getvalue()

class DataObject(object):
    def __init__(self, d):
        self.__dict__.update(d)

        
def main():
    if len(sys.argv) != 2:
        print 'specify input file'
        exit()

    startTime = time.clock()

    global fin, fout
    fin = open(sys.argv[1])
    fout = open(os.path.splitext(sys.argv[1])[0]+'.out', 'w')

    numCases = int(next(fin))
    inputs = (DataObject(read(i)) for i in range(numCases))


    if parallel:
        pool = Pool(4)
        results = pool.imap(solve, inputs)
    else:
        results = imap(solve, inputs)

    for caseNo, result in enumerate(results):
        fout.write('Case #%s: '%(caseNo+1))
        fout.write(result)

    fin.close()
    fout.close()

    print 'it took %.1fs'%(time.clock()-startTime)

if __name__ == "__main__":
    main()