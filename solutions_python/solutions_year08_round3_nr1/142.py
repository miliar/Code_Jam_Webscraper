#!/usr/bin/python

import math
from optparse import OptionParser

def main():
    USAGE = "usage: %prog [option]"
    parser = OptionParser(usage=USAGE)
    (options, args) = parser.parse_args()

    file_in = args[0]
    fi = file(file_in, 'r')
    N = int(fi.readline().rstrip('\n'))

    solution = [0]*N
    for n in range(0, N):
        pass
        #Parse Input for particular testcase
        line = fi.readline().rstrip('\n').split(' ')
        P = int(line[0])
        K = int(line[1])
        L = int(line[2])
        line = fi.readline().rstrip('\n').split(' ')
        freq = []
        for i in range(0, L):
            freq.append([i, int(line[i])])

        freq.sort(lambda x, y: cmp(y[1], x[1]))

        keys = []
        for i in range(0, K):
            keys.append([0]*P)

        #assignkey
        
        for j in range(0, P):
            for i in range(0, K):
                if j*K +i < len(freq):
                    keys[i][j] = freq[j*K +i][1]
                    solution[n] += freq[j*K +i][1]*(j+1)

        #
        #Find Solution
        #

    fi.close()

    #write output
    file_out = file_in[:len(file_in)-3] + ".out"
    fo = file(file_out, 'w')
    for n in range(0, N):
        if solution[n] != 'impossible':
            fo.write("Case #%d: %d\n" %(n+1, solution[n]))
        else:
            fo.write("Case #%d: impossible\n" %(n+1))
    fo.close()

if __name__ == "__main__":
    main()
