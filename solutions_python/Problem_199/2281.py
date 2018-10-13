#!/usr/env/bin python3
import sys

pancakes = []
flippers = []

with open(sys.argv[1]) as f:
    T = int(f.readline())
    for line in f.readlines():
        split = line.split()
        pancakes += [list(split[0])]
        flippers += [int(split[1])]

def calc(pancake, flipper):
    flips = 0
    for i in range(len(pancake)):
        if pancake[i] == '-' and len(pancake) > (flipper + i - 1):
            flips += 1
            for j in range(i, flipper + i):
                if pancake[j] == '-':
                    pancake[j] = '+'
                else:
                    pancake[j] = '-'
    if '-' in pancake:
        return -1
    else:
        return flips

for t in range(T):
    pancake = pancakes[t]
    flipper = flippers[t]
    flips = calc(pancake, flipper)

    out = "Case #{}: ".format(t + 1)
    if flips == -1:
        out += "IMPOSSIBLE"
    else:
        out += str(flips)
    print(out)
