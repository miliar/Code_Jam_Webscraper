#!/usr/bin/python3

import sys
import math

nRounds = int(sys.stdin.readline().strip())

for r in range(0, nRounds):
    strInput = sys.stdin.readline().strip()
    iIng = int(strInput.split()[0], 10)
    iPac = int(strInput.split()[1], 10)
    recipe = []
    for _ in sys.stdin.readline().strip().split():
        recipe.append(int(_, 10))
    pacs = []
    for i in range(0, iIng):
        pacs.append([])
        for _ in sys.stdin.readline().strip().split():
            pacs[i].append(int(_, 10))
        pacs[i].sort()
    iKits = 0

    max_idx = 0
    indices = [0] * iIng
    while max_idx < iPac:
        tmp = []
        for i in range(0, iIng):
            tmp.append(pacs[i][indices[i]] / recipe[i])
        max_value = max(tmp)
        max_id = tmp.index(max_value)
        min_value = min(tmp)
        min_id = tmp.index(min_value)
        blFound = False
        if (max_value - min_value) / max_value > 0.21:  # leave some margin
            blFound = False
        else:
            for i in range(math.floor(min_value), math.ceil(max_value) + 1):
                blOK = True
                for j in range(0, iIng):
                    expected = recipe[j] * i
                    iDiff = abs(pacs[j][indices[j]] - expected)
                    if iDiff > int(expected / 10):
                        blOK = False
                        break
                if blOK:
                    blFound = True
                    break
        if blFound:
            iKits = iKits + 1
            for i in range(0, iIng):
                indices[i] = indices[i] + 1
            max_idx = max_idx + 1
        else:
            # forward minimum
            indices[min_id] = indices[min_id] + 1
            if indices[min_id] > max_idx:
                max_idx = indices[min_id]
    print("Case #{}: {}".format(r+1, iKits))
    sys.stdout.flush()
