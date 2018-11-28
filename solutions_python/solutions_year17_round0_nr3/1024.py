import sys
import math


def solve(N, K):
    if N == K:
        return 0, 0
    y = 2 ** int(math.log(K, 2))
    a, b = divmod(N - (y - 1), y)
    if K - y > b - 1:
        return int((a - 1) / 2.0 + .5), (a - 1) / 2
    else:
        return int(a / 2.0 + .5), a / 2


with open(sys.argv[1], "r") as f:
    file = f.readlines()
    T = int(file.pop(0))
    for t in range(T):
        line = file.pop(0).strip()
        N, K = map(int, line.split(' '))
        a, b = solve(N, K)
        print "Case #%d: %d %d" % (t + 1, a, b)
