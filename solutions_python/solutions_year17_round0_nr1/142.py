#!/usr/bin/python

import sys

def solve(ps, k):
    f = 0
    for i in range(0, len(ps) - k + 1):
        if ps[i] == 0:
            flip(ps, i, k)
            f += 1

    if all_smiles(ps):
        return f
    else:
        return -1

def flip(ps, i, k):
    for j in range(i, i + k):
        ps[j] = ps[j] ^ 1

def all_smiles(ps):
    for p in ps:
        if p == 0:
            return False
    return True

def main():
    T = int(next(sys.stdin))
    for t, line in enumerate(sys.stdin, 1):
        pancakes, k = line.split()
        k = int(k)
        pancakes = [(1 if p == '+' else 0) for p in pancakes]
        result = solve(pancakes, k)
        if result == -1:
            print "Case #{}: IMPOSSIBLE".format(t)
        else:
            print "Case #{}: {}".format(t, result)

main()
