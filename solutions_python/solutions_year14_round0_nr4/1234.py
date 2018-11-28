#!/usr/bin/env python
import sys


def problem(fi):
    r1 = int(fi.readline().strip())
    arr1 = [float(f) for f in fi.readline().strip().split(' ')]
    arr2 = [float(f) for f in fi.readline().strip().split(' ')]
    return arr1, arr2


def solve(params, fo, i):
    arr1, arr2 = params
    arr1.sort()
    arr2.sort()
    arrc1 = arr1[:]
    arrc2 = arr2[:]
    wdw = 0
    ww = 0

    while arrc1:
        min1 = arrc1[0]
        if min1 > arrc2[len(arrc2) - 1]:
            del arrc1[0]
            del arrc2[0]
            ww += 1
        else:
            for j, min2 in enumerate(arrc2):
                if min2 > min1:
                    del arrc1[0]
                    del arrc2[j]
                    break


    while arr1:
        if arr1[0] < arr2[0]:
            del arr1[0]
            del arr2[len(arr2) - 1]
        else:
            del arr1[0]
            del arr2[0]
            wdw += 1

    return wdw, ww


if __name__ == '__main__':
    with open(sys.argv[1]) as fi, open(sys.argv[2], 'w') as fo:
        total = int(fi.readline().strip())
        for i in range(total):
            res = solve(problem(fi), fo, i)
            fo.write('Case #{0}: {1} {2}\n'.format(i + 1, res[0], res[1]))
            fo.flush()
