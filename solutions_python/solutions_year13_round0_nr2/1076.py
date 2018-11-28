import sys

def uniq(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if x not in seen and not seen_add(x)]

def solve(ft, sizex, sizey):
    maxy = []
    for y in range(sizey):
        maxy.append(max(ft[y]))
    maxx = []
    for x in range(sizex):
        m = 0
        for y in range(sizey): m = max(m, ft[y][x])
        maxx.append(m)

    heights = uniq(sorted([h for line in ft for h in line]))
    # print(heights)
    heights.reverse()
    f = [[heights[-0] for col in range(sizex)] for row in range(sizey)]
    # for l in f:
    #     print(l)

    for h in heights[1:]:
    #     print(h)
        for y in range(sizey):
            if maxy[y] <= h:
                for x in range(sizex): f[y][x] = h
        for x in range(sizex):
            if maxx[x] <= h:
                for y in range(sizey): f[y][x] = h

    # for l in f:
    #     print(l)

    for y in range(sizey):
        for x in range(sizex):
            if f[y][x] != ft[y][x]: return "NO"

    return "YES"

numcases = int(sys.stdin.readline())
for c in range(numcases):
    sizey, sizex = [int(x) for x in sys.stdin.readline().split()]
    f = []
    for y in range(sizey):
        linex = [int(h) for h in sys.stdin.readline().split()]
        f.append(linex)
    print("Case #%d: %s" % (c+1, solve(f, sizex, sizey)))
