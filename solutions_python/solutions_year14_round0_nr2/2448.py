from sys import stdin
import math

file = stdin


def read_line():
    return file.readline()


def read_int():
    return int(read_line())


def iteration(c, f, x):
    return max(int(math.ceil(x/float(c) - 1 - 2/float(f))), 0)

def process(c, f, x):
    n = iteration(c, f, x)
    total = 0
    for i in range(n):
        total = total + c / (2 + i * float(f))
    total = total + x / (2 + n * f)
    return total

cases = read_int()
for case_no in range(1, cases + 1):
    [c, f, x] = map(lambda z: float(z), read_line().split())
    old = process(c, f, x)
    print("Case #{0}: {1:.7f}".format(case_no, old))

