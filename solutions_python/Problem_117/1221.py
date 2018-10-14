import sys

with open(sys.argv[1]) as h:
    c = int(h.readline())
    def test():
        splits = h.readline()[:-1].split(' ')
        Y, X = map(int, splits)
        hor = []
        print 'X', X, 'Y', Y
        for _ in range(Y):
            spl = map(int,h.readline()[:-1].split(' '))
            print spl
            hor.append(spl)
        ver = [[hor[y][x] for y in range(Y)] for x in range(X)]
        for x in range(X):
            print 'x', x
            for y in range(Y):
                print 'y', y
                if hor[y][x] != max(ver[x]) and hor[y][x] != max(hor[y]):
                    return 'NO'
        return 'YES'
    with open(sys.argv[1][:-2] + 'out', 'w') as f:
        res = '\n'.join(['Case #%s: %s' % (i, test()) for i in range(1, c + 1)])
        print res
        f.write(res)
