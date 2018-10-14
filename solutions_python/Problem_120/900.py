from sys import argv
import math

script, filename = argv

f = open(filename)

T = int(f.readline())


def check(r, total):
    i = 0
    t = 2*r + 1
    while t <= total:
        i += 1
        r += 2
        t += 2 * r + 1
    return i

"""    if (r > 1):
        total += (6 + 4 * (r - 2)) * r / 4
    return int(math.floor((math.sqrt(1 + 8 * total) - 1) / 4))
"""

for t in range(T):
    (x, y) = map(int, f.readline().split())

    print 'Case #{0}: {1}'.format(t + 1, check(x, y))
