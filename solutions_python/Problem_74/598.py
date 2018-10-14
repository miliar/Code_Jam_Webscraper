#!/usr/bin/env python

from sys import stdin

def solve(buttons):
    posO, posB = 1, 1
    stepO, stepB = 0, 0
    for (i, j) in buttons:
        if i == 'O':
            stepO += abs(posO - j)
            if stepO < stepB:
                stepO = stepB
            stepO += 1
            posO = j
        else:
            stepB += abs(posB - j)
            if stepB < stepO:
                stepB = stepO
            stepB += 1
            posB = j
    return max(stepO, stepB)

def main():
    T = int(stdin.readline())
    for i in range(T):
        line = stdin.readline().split()
        N = int(line.pop(0))
        buttons = []
        for j in range(N):
            buttons.append((line.pop(0), int(line.pop(0))))
        print "Case #{0}: {1}".format(i+1, solve(buttons))

main()
