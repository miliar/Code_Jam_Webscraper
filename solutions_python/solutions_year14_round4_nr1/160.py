def solve(C, fs):
    fs.sort()
    total = 0
    head = 0
    tail = len(fs)-1
    while tail > head:
        if fs[tail] + fs[head] <= C:
            head += 1
        tail -= 1
        total += 1
    if tail == head:
        total += 1
    return total
from sys import stdin

cases = int(stdin.readline())
for c in range(cases):
    N, C = map(int, stdin.readline().split())
    fs = map(int, stdin.readline().split())
    print "Case #%d: %d" % (c+1, solve(C, fs))
