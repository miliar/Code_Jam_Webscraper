import sys
import math

def test(i, pancakes, k):
    r = pancakes[i][0]
    new_pancakes = pancakes[:i] + pancakes[i+1:]
    new_pancakes = [p for p in new_pancakes if p[0] <= r]
    if len(new_pancakes) < k - 1:
        return 0

    total = pancakes[i][2] + math.pi * r * r
    for p in new_pancakes[:(k-1)]:
        total += p[2]
    return total



T = int(sys.stdin.readline())

for t in xrange(T):
    line = sys.stdin.readline()
    n, k = map(int, line.split())

    pancakes = []
    for i in xrange(n):
        line = sys.stdin.readline()
        r, h = map(int, line.split())
        a = 2 * math.pi * r * h
        pancakes.append((r, h, a))
    pancakes.sort(key = lambda x: x[2], reverse = True)

    best = 0
    for i in xrange(n):
        temp = test(i, pancakes, k)
        best = max(best, temp)

    print("Case #%d: %f" % (t+1, best))

