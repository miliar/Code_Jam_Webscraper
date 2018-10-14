"""
This script may use libraries publicly available at: https://github.com/grokit/dcore.

Does this solution solve:
   Small: ?.
   Big:   ?.
"""

import dcore.gcj_boot as boot

def readProblem(fh):
    a, b = fh.readline().strip().split()

    A = []
    for i in range(len(b)):
        A.append(int(b[i]))
    return A 

def solve(p):
    A = p

    numNeed = 0
    t = 0
    for i in range(len(A)):
        if t < i:
            numNeed += i-t
            t = i

        t += A[i]

    return numNeed

boot.solve(solve, readProblem, '.*large')
