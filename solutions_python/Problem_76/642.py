#!/usr/bin/python

input = [1, 2, 3, 4, 5]
#input = [3, 5, 6]

def xorsum(s): return reduce(lambda x,y: x^y, s, 0)

def doIt(input):
    best = 0
    for c in range(1, (2**len(input))-1):
        a = set()
        b = set()

        x = 1
        for i in input:
            if c & x:
                a.add(i)
            else:
                b.add(i)
            x <<= 1

        if xorsum(a) == xorsum(b):
            best = max(best, max(sum(a), sum(b)))

    if best == 0:
        return "NO"
    else:
        return str(best)

import fileinput
f = fileinput.input()
f.next() # number of cases

case = 1
for line in f:
    answer = doIt(map(int, f.next().strip().split()))
    print("Case #%d: %s" % (case, answer))
    case += 1
