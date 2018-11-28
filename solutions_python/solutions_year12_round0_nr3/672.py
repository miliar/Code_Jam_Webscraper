# Google Code Jam 2012 qualification round C.

import sys
def doCase(a, b):
    found = {}
    numDigits = len(str(a))
    # Find pairs (n,m)
    for n in xrange(a,b):
        for numRot in xrange(1, numDigits):
            m = int(str(n)[-numRot:] + str(n)[:-numRot])
            if m > n and m <= b:
                found[(n, m)] = 1
    return len(found)

def run():
    file = open(sys.argv[1])
    numCases = int(file.readline())
    for case in range(1, numCases+1):
        (a,b) = map(int, file.readline().split())
        answer = doCase(a, b)
        print 'Case #{0}: {1}'.format(case, answer)
run()
