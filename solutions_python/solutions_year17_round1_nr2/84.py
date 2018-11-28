from math import *

[t, ] = [int(x) for x in input().split()]

def process_test(num):
    [n, p] = [int(x) for x in input().split()]
    rs = [int(x) for x in input().split()]
    packs = []
    for _ in range(n):
        packs.append(sorted([int(x) for x in input().split()]))

    multi = 1
    res = 0
    while True:
        changed = False

        for i in range(len(packs)):
            while True:
                if packs[i][0] < ceil(multi * rs[i] * 0.9):
                    packs[i] = packs[i][1:]
                    if len(packs[i]) == 0:
                        print("Case #", num, ": ", res, sep='')
                        return
                elif packs[i][0] > floor(multi * rs[i] * 1.1):
                    while packs[i][0] > floor(multi * rs[i] * 1.1):
                        multi += 1
                    changed = True
                else:
                    break
        if not changed:
            res += 1
            for i in range(len(packs)):
                packs[i] = packs[i][1:]
                if len(packs[i]) == 0:
                    print("Case #", num, ": ", res, sep='')
                    return

for num in range(1, t+1):
    process_test(num)