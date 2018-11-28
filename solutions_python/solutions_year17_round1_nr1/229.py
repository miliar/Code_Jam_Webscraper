import sys

t = int(sys.stdin.readline().strip())
for ti in xrange(t):
    line = sys.stdin.readline().split()
    r = int(line[0])
    c = int(line[1])
    g = []
    for ri in xrange(r):
        g.append(list(sys.stdin.readline().strip()))

    for ri in xrange(r):
        letter = ''
        for ci in xrange(c):
            if g[ri][ci] == '?' and letter != '':
                g[ri][ci] = letter
                continue
            if g[ri][ci] != '?':
                if letter == '':
                    for cj in xrange(ci):
                        g[ri][cj] = g[ri][ci]
                letter = g[ri][ci]

    li = -1
    for ri in xrange(r):
        if g[ri][0] == '?' and li != -1:
            g[ri] = g[li]
            continue
        if g[ri][0] != '?':
            if li == -1:
                for rj in xrange(ri):
                    g[rj] = g[ri]
            li = ri

    case = "Case #%d: " % (ti + 1)
    print case
    for l in g:
        print ''.join(l)

