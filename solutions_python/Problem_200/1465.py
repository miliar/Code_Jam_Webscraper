import sys
input = open(sys.argv[1])


def tidy(x):
    t = 9
    while x and t >= x % 10:
        t = x % 10
        x //= 10
    return x == 0


def solve(val):
    for x in range(val, 1, -1):
        if tidy(x):
            return x
    return val

for i, v in enumerate([int(x) for x in input.readlines()][1:]):
    print ("Case #%d: %d" % (i + 1, solve(v)))
