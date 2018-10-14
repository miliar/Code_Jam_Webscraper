#-*- encoding: utf-8 -*-

import sys

X, North, West, East, South = range(5)
dh = [-1, 0, 0, 1]
dw = [0, -1, 1, 0]

def next(region, h, w):
    ret = h, w
    cur = region[h][w]
    lowest = cur
    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]
        if nh < 0 or nh >= H or nw < 0 or nw >= W:
            pass
        else:
            candidate = region[nh][nw]
            if candidate < min(cur, lowest):
                ret = nh, nw
                lowest = candidate
    return ret

def find_waterpaths(region):
    paths = { }
    H, W = len(region), len(region[0])
    for h in xrange(H):
        for w in xrange(W):
            path = [(h, w), next(region, h, w)]
            if path[0] != path[1]:
                paths.setdefault(path[0], []).append(path[1])
                paths.setdefault(path[1], []).append(path[0])
    return paths

def mark(region, paths):
    H, W = len(region), len(region[0])
    basin = 'a'
    for h in xrange(H):
        for w in xrange(W):
            q = [(h, w)]
            cur = region[h][w]
            if not cur in range(10): continue
            while len(q) > 0:
                h, w = q.pop()
                region[h][w] = basin
                next_paths = [(y, x) for y, x in paths.get((h, w), []) if region[y][x] in range(10)]
                q.extend(next_paths)
            basin = chr(ord(basin) + 1)

    return paths


def solve(region):
    waterpaths = find_waterpaths(region)
    mark(region, waterpaths)
    return region

if __name__ == '__main__':
    case_n = int(sys.stdin.readline().strip())
    for case in xrange(case_n):
        H, W = (int(x) for x in sys.stdin.readline().strip().split())
        region = [[int(x) for x in sys.stdin.readline().strip().split()] for y in xrange(H)] # h, w
        solution = solve(region)
        print 'Case #%d:' % (case+1)
        print '\n'.join(' '.join(str(x) for x in row) for row in solution)
