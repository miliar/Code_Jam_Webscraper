import math
import sys


inp = sys.stdin

T = int(inp.readline())
for case_number in range(1, T + 1):
    r, t = map(int, inp.readline().split())
    D = (2 * r - 1) ** 2 + 8 * t
    n_max = int((1 - 2 * r + math.sqrt(D)) / 4.0)
    if 2 * n_max ** 2 + 2 * r * n_max - n_max > t:
        n_max -= 1
    print 'Case #%d: %d' % (case_number, n_max)
