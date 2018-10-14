#pylint: disable=missing-docstring,invalid-name
import sys
import os
import math

def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    if a > 0:
        return a
    return 1

def decide(P, Q):
    # first make P/Q be in lowest terms
    d = gcd(P, Q)
    P = P / d
    Q = Q / d
    # now Q should be 2**n, or it's impossible
    if Q == 1:
        return 0
    n = int(math.log(Q) / math.log(2))
    if 2**n != Q:
        return 'impossible'
    # now P means how many ancestors were pure Elves n generations ago (n - P were pure humans);
    # we also note that it's not important how our ancestors were ordered. So we can go from
    # ancestors to our time breeding pure Elves only log2(P) times
    return n - int(math.log(P) / math.log(2))

def main():
    with open(sys.argv[1], 'r') as inp, open('%s.out' % (os.path.splitext(sys.argv[1])[0]), 'w') as out: #pylint: disable=line-too-long
        T = int(inp.readline())
        for t in xrange(T):
            P, Q = [int(x) for x in inp.readline().strip().split('/')]
            out.write('Case #%s: %s\n' % (t + 1, decide(P, Q)))

if __name__ == '__main__':
    main()
