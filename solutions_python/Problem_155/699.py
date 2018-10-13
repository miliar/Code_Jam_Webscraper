def solveTestcase(nr):
    n, tab = raw_input().split()
    tab = [int(i) for i in tab]
    res = 0
    sum = 0
    for i, val in enumerate(tab):
        while sum + res < i:
            res += 1
        sum += val
    print "Case #{}: {}".format(nr, res)

z = int(raw_input())
for i in range(1, z + 1):
    solveTestcase(i)
