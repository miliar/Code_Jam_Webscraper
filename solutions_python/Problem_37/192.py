from __future__ import with_statement
import sys

def happy_i(x, n):
    tmp = 0
    while x > 0:
        x, d = divmod(x, n)
        tmp += d * d
    return tmp

def is_happy(x, n):
    if x not in H[n]:
        H[n][x] = happy_i(x, n)
        H[n][x] = is_happy(H[n][x], n)
    return True if H[n][x] is True else False

with open(sys.argv[1]) as f:
    num_cases = int(f.readline())

    H = dict(( (b, {1: True}) for b in xrange(2, 11) ))
    
    for c in xrange(num_cases):
        bases = map(int, f.readline().split())
        i = 2
        while True:
            if all(map(lambda b: is_happy(i, b), bases)):
                break
            i += 1
        print "Case #%d: %d" % (c+1, i)
