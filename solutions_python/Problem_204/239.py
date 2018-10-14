#!/usr/local/bin/python
import sys
import heapq
import math

def overlaps((l1, h1), (l2, h2)):
    if (l1 > h1 or l2 > h2):
        return False
    if (l2 <= h1 and h1 <= h2):
        return True
    if (l1 <= h2 and h2 <= h1):
        return True
    return False 

def solve(count):
    N, P = sys.stdin.readline().split()
    N = int(N)
    P = int(P)
    amounts = sys.stdin.readline().split()
    amounts = [int(n) for n in amounts]

    # maps ingredient amounts to acceptable values
    ingredientPackages = [0] * N;
    for i in range(N):
        packages = [int(n) for n in sys.stdin.readline().split()]
        packages = [(int(math.ceil(n / (amounts[i] * 1.1))), int(math.floor(n / (amounts[i] * 0.9)))) for n in packages]
        ingredientPackages[i] = packages
    packages = ingredientPackages

    if (N == 1):
        packages = packages[0]
        count = 0
        for (l, h) in packages:
            if l <= h and h > 0:
                count += 1
        print "Case #{}: {}".format(case + 1, count)
        return

    def calculate(firstPackages, secondPackages):
        if len(firstPackages) == 0:
            return 0
        package = firstPackages[0]
        rest = firstPackages[1:]
        maxNum = calculate(rest, secondPackages)
        for package2 in secondPackages:
            #print package, package2
            if (overlaps(package, package2)):
                newSeconds = secondPackages[:]
                newSeconds.remove(package2)
                #print rest, newSeconds
                maxNum = max(maxNum, calculate(rest, newSeconds)+1)
        return maxNum

    answer = calculate(packages[0], packages[1])
    print "Case #{}: {}".format(case + 1, answer)

cases = int(sys.stdin.readline())
for case in range(cases):
    solve(case)
