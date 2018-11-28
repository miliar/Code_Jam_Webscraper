#!/usr/bin/env python3

from sys import stdin

def solve(shyness):
    clapping = 0
    invited = 0
    for shy, c in enumerate(shyness):
        i = ord(c) - ord('0')
        add = max(shy - clapping, 0)
        invited += add
        clapping += add + i
    return invited

if __name__ == '__main__':
    ncases = int(stdin.readline())
    for i in range(ncases):
        [_smax, shyness] = stdin.readline().split()
        print("Case #{}: {}".format(i + 1, solve(shyness)))
