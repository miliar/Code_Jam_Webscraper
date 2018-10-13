def cuttingCost(present, desired):
    parts = present / desired + (1 if present % desired != 0 else 0)
    return parts - 1

def costWithSetMaxPartLength(maxLength, tab):
    res = 0
    for i in tab:
        res += cuttingCost(i, maxLength)
    res += maxLength
    return res

def solveTC(nr):
    n = int(raw_input())
    tab = [int(i) for i in raw_input().split()]
    res = min([costWithSetMaxPartLength(i, tab) for i in range(1, 1001)])
    print "Case #{}: {}".format(nr, res)

z = int(raw_input())
for i in range(1, z + 1):
    solveTC(i)

