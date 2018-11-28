import sys

stdinrl = sys.stdin.readline

def fill(k, N, groups, startidx, cache):
    if cache[startidx] != None:
        return cache[startidx]
    current = k
    i = startidx
    while current >= groups[i]:
        current -= groups[i]
        i = (i+1)%N
    cache[startidx] = i, k-current
    return cache[startidx]

def solvecase(idx):
    R, k, N = map(int, stdinrl().split())
    groups = map(int, stdinrl().split())
    total = 0
    startidx = 0
    s = sum(groups)
    if k > s:
        print "Case #%d: %d" % (idx, s*R)
        return
    cache = [None]*N
    for i in range(R):
        startidx, value = fill(k, N, groups, startidx, cache)
        total += value
    print "Case #%d: %d" % (idx, total)

T = int(stdinrl())
for i in range(1, T+1):
    solvecase(i)
