#!/usr/bin/env python

from sys import stdin, stdout, stderr

if __name__ == '__main__':  
    T = int(stdin.readline())
    for t in range(T):
        tokens = stdin.readline().split()
        strA, strB = tokens[0], tokens[1]
        A, B = int(strA), int(strB)
        strLength = len(strA)

        result = 0
        for N in range(A, B + 1):
            strN = str(N)
            candidates = set()
            for i in range(1, strLength):
                rotN = int(strN[i : ] + strN[ : i])
                if N < rotN and rotN <= B:
                    candidates.add(rotN)
            result += len(candidates)

        stdout.write('Case #%d: %d\n' % (t + 1, result))

