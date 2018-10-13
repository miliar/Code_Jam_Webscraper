import sys


def solve(r, t):
    result = 0
    area = (pow(r + 1, 2) - pow(r, 2))

    while t >= area:
        t -= area
        r += 2
        area = (pow(r + 1, 2) - pow(r, 2))
        result += 1

    return result


#stream = open("in.txt")
stream = sys.stdin
T = int(stream.readline())
for c in range(1, T + 1):
    r, t = [int(x) for x in stream.readline().split()]
    print "Case #%d: %d" % (c, solve(r, t))