from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def nineUpto(n, d):
    nines = 1
    while(nines < d):
        nines = nines * 10 + 1
    nines *= 9

    n -= n % (d*10)
    n += nines
    return n

nCase = int(input())
eprint("There are %d cases" % nCase)
for caseI in range(1, nCase + 1):
    ns = input()
    eprint("Number : {}".format(ns))

    d = 1
    while(ns / d >= 1):
        d2 = d * 10
        if((ns / d2) % 10 > (ns / d) % 10):
            # All the previous digit can be 9 now
            ns -= d2
            ns = nineUpto(ns, d)
        d = d2

    eprint("Case #{}: {}".format(caseI, ns))
    print("Case #{}: {}".format(caseI, ns))
          # check out .format's specification for more formatting options

