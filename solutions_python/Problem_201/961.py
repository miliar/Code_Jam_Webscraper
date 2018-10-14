from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


nCase = int(raw_input())
eprint("There are %d cases" % nCase)
for caseI in range(1, nCase + 1):
    n, k = [int(s) for s in raw_input().split(" ") ]
    eprint("Input : n: {}, k: {}".format(n, k))

    r = n
    l = n
    while(k > 1):
        pos = n / 2 + n%2

        l = pos - 1
        r = pos - n%2

        k -= 1 # One has been placed
        if(k%2):
            n = max(l,r)
            k = k/2 + 1
        else:
            n= min(l,r)
            k = k/2

    pos = n / 2 + n%2

    l = pos - 1
    r = pos - n%2


    sol = "Case #{}: {} {}".format(caseI, max(l,r), min(r,l))
    eprint(sol)
    print(sol)

