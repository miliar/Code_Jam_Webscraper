import sys
import fileinput
from array import *

def c(S, perm):
    k = len(perm)
    b = 0
    p = 0

    last = S[perm[0]]
    test = last
    count = 1
    for i in range(1, len(S)):
        next = S[b + perm[p]]
        test += next
        if next != last:
            count += 1
            last = next

        p += 1
        if p == k:
            b += k
            p = 0

    return count

def recSolve(k, rem, sofar, S):
    if len(rem) == 0:
        return c(S, sofar.tolist())

    m = 10000000
    copy = array('i', rem)
    elem = copy.pop(0)
    for i in range(0, len(sofar)+1):
        other = array('i', sofar)
        other.insert(i, elem)
        val = recSolve(k, copy, other, S)
        if val < m:
            m = val

    return m

def solve(k, S):
    return recSolve(k, array('i', range(0, k)), array('i'), S)

if __name__ == '__main__':
    lines = fileinput.input(sys.argv[1])
    N = int(lines.readline())
    for i in range(1, N+1):
        k = int(lines.readline())
        S = lines.readline()
        out = solve(k, S)

        print "Case #%d: %d" % (i, out)
