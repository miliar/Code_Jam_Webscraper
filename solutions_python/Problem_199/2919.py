#!/usr/bin/python3

def flip(cakes, n):
    cakes = list(cakes)
    for i in range(0, n):
        if cakes[i] == '-':
            cakes[i] = '+'
        else:
            cakes[i] = '-'
    return ''.join(cakes)

def flipper(cakes, n):
    flips = 0
    while len(cakes) > 0:
        if len(cakes) < n:
            return "IMPOSSIBLE"
        while len(cakes) > 0 and cakes[0] == '+':
            cakes = cakes[1:]
        if len(cakes) == 0:
            return str(flips)
        if len(cakes) < n:
            continue
        cakes = flip(cakes, n)
        flips += 1
    return str(flips)


# input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, m = [s for s in input().split(" ")]  # read a list of integers, 2 in this case
    m = int(m)

    print("Case #{}: {}".format(i, flipper(n, m)))
    # check out .format's specification for more formatting options

