import sys
from collections import deque

def readline():
    return sys.stdin.readline().strip()

def xorsum(v):
    return reduce(lambda x, y: x ^ y, v, 0)

def permute(elem):
    for i in xrange(1, 2 ** len(elem) - 1):
        perm = []
        other = []
        for j in range(len(elem)):
            if i & 1 == 1:
                perm.append(elem[j])
            else:
                other.append(elem[j])
            i >>= 1
        yield perm, other

def solve(line):
    elem = [int(x) for x in line.split()]
    results = []
    for perm, other in permute(elem):
        if xorsum(perm) == xorsum(other):
            results.append(max(sum(perm), sum(other)))
    if len(results) > 0:
        return str(max(results))
    return "NO"

def main():
    n_inputs = int(readline())
    for i in range(n_inputs):
        n = readline()
        print "Case #%d: %s" % (i + 1, solve(readline()))

if __name__ == "__main__":
    main()
