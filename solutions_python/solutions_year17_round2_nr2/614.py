from sys import setrecursionlimit
setrecursionlimit(100000)

def ok(i, j):
    #todo: colours collide
    return i != j

cache = {}

def f(p, i, first):
    hash = tuple(p + [i,first])
    if hash in cache:
        return cache[hash]
    if sum(p) == 1:
        idx = p.index(1)
        if idx == first or idx == i:
            return False
        return [idx]
    if sum(p) < 2*max(p)-8:
        return False
    for j, cc in enumerate(p):
        if cc > 0 and ok(j, i):
            p[j] -= 1
            path = f(p, j, first)
            if path:
                cache[hash] = path + [j]
                return path + [j]
            p[j] += 1
    cache[hash] = False
    return False

#data = iter(open("in.txt").read().splitlines())
data = iter(open("B-small-attempt1.in").read().splitlines())
T = int(next(data))
for caseNum in range(1, T + 1):
    n, R, O, Y, G, B, V = map(int, next(data).split())
    h = [(R, "R"), (Y, "Y"), (B, "B")]
    p = [R,Y,B]
    first = 0
    if not p[0]:
        first = 1
        if not p[1]:
            first = 2
    ans = "IMPOSSIBLE"
    p[first] -= 1
    path = f(p, first, first)
    if path:
        path = path + [first]
        for i in range(len(path)):
            path[i] = "RYB"[path[i]]
        ans = "".join(path)
    print "Case #%d: %s" % (caseNum, ans)