from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def swap(bits, s, i):
    #eprint("Before Swap bits index {}, bits {}".format(i, "".join([str(r) for r in bits])))
    for x in range(i, i+s):
        bits[x] = 1 - bits[x]
    #eprint("After Swap bits index {}, bits {}".format(i, "".join([str(r) for r in bits])))

def solve(bits, s, i):
    if(sum(bits) == len(bits)):
        return 0
    elif i+s > len(bits) :
        return sys.maxint
    else:
        swap(bits, s, i)
        countA = solve(bits, s, i+1) + 1

        swap(bits, s, i)
        countB = solve(bits, s, i+1)
        #eprint("Swapped: {}, not swapped: {}".format(countA, countB))
        return min(countA, countB)

nCase = int(raw_input())
eprint("There are %d cases" % nCase)
for caseI in range(1, nCase + 1):
    pancakes, s = raw_input().split(" ")
    s = int(s)
    bits = [0 if p == '-' else 1 for p in pancakes]

    eprint("Input : s: {}, bits: {}".format(s, ''.join([str(b) for b in bits])))

    count = solve(bits, s, 0)
    eprint("Sol: {}".format(count))

    if count < 100000:
        result = str(count)
    else:
        result = "IMPOSSIBLE"

    sol = "Case #{}: {}".format(caseI, result)
    eprint(sol)
    print(sol)

