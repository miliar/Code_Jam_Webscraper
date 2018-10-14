if __name__ == '__main__':
    n = int(raw_input())
    for case in xrange(n):
        r,c = map(int, raw_input().split())
        cake = [list(raw_input()) for _ in xrange(r)]
        seen = set([])
        for row in xrange(r):
            for col in xrange(c):
                cell = cake[row][col]
                if cell == '?': continue
                if cell in seen: continue
                seen.add(cell)

                x,y,w,h = (col,row,1,1)
                while x > 0 and cake[y][x-1] == '?':
                    x -= 1
                    w += 1
                while x+w < c and cake[y][x+w] == '?':
                    w += 1

                while y > 0:
                    bad = False
                    for xi in xrange(x,x+w):
                        if cake[y-1][xi] != '?': bad = True
                    if bad: break
                    y -= 1
                    h += 1
                while y+h < r:
                    bad = False
                    for xi in xrange(x,x+w):
                        if cake[y+h][xi] != '?': bad = True
                    if bad: break
                    h += 1

                for a in xrange(x, x+w):
                    for b in xrange(y, y+h):
                        cake[b][a] = cell

        print 'Case #%d:' % (case+1)
        for row in cake:
            print ''.join(row)
