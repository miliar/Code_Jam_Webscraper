#!/usr/bin/python3
from sys import argv

def main(args):
    with open(args[1]) as inp, open(args[2], 'w') as out:
        cases = int(inp.readline())
        for case in range(0, cases):
            line = inp.readline()
            [c, f, x] = [float(x) for x in line.split()]
            ans = solve(c, f, x)
            out.write("Case #%d: %.7f\n" % ((case + 1), ans))

def solve(c, f, x):
    most = x / c
    best = x / 2.0
    for i in range(1, int(most) + 1):
        rate = 2.0 + (i * f)
        time = x / rate
        for j in range(0, i):
            time += (c / (2.0 + (j) * f))

        best = min(best, time)

    return best
        

if __name__ == '__main__':
    main(argv)
