import sys
sys.setrecursionlimit(20000)
# f = open('inp'); raw_input = f.readline
t = int(raw_input())

def go(here):
    if here == len(locations): 
        return True
    num, y, x = locations[here]
    if explained[y][x]: return go(here + 1)

    all_v, all_h = True, True
    for i in xrange(h):
        if not explained[i][x] and heights[i][x] != num:
            all_v = False
            break
    for j in xrange(w):
        if not explained[y][j] and heights[y][j] != num:
            all_h = False
            break
    if all_v:
        for i in xrange(h):
            explained[i][x] += 1
        if go(here + 1): return True
        for i in xrange(h):
            explained[i][x] -= 1

    if all_h:
        for j in xrange(w):
            explained[y][j] += 1
        if go(here + 1): return True
        for j in xrange(w):
            explained[y][j] -= 1

    return False

for c in xrange(t):
    print 'Case #%d:' % (c+1),
    h, w = map(int, raw_input().split())
    heights = [map(int, raw_input().split())
               for i in xrange(h)]
    explained = [[0] * w for i in xrange(h)]
    locations = [(heights[i][j], i, j)
                 for i in xrange(h)
                 for j in xrange(w)]
    locations = sorted(locations)

    if go(0):
        print 'YES'
    else:
        print 'NO'
