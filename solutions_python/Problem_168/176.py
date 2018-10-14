from collections import Counter
t = int(raw_input())
for kei in xrange(1, t+1):
    r, c = [int(x) for x in raw_input().split()]
    grid = [raw_input() for i in xrange(r)]
    d = {'^': 0, '>': 1, 'v': 2, '<': 3}
    arrows = []
    mincol = {}
    minrow = {}
    maxcol = {}
    maxrow = {}
    for i in xrange(r):
        for j in xrange(c):
            if grid[i][j] != '.':
                if i not in mincol:
                    mincol[i] = j
                if i not in maxcol:
                    maxcol[i] = j
                if j not in minrow:
                    minrow[j] = i
                if j not in maxrow:
                    maxrow[j] = i
                mincol[i] = min(mincol[i], j)
                maxcol[i] = max(maxcol[i], j)
                minrow[j] = min(minrow[j], i)
                maxrow[j] = max(maxrow[j], i)
    def result():
        tot = 0
        for i in xrange(r):
            for j in xrange(c):
                if grid[i][j] != '.':
                    avail = set()
                    if mincol[i] < j:
                        avail.add('<')
                    if minrow[j] < i:
                        avail.add('^')
                    if maxcol[i] > j:
                        avail.add('>')
                    if maxrow[j] > i:
                        avail.add('v')
                    if not avail:
                        return "IMPOSSIBLE"
                    if grid[i][j] not in avail:
                        tot += 1
        return tot
    print("Case #{}: {}".format(kei, result()))
