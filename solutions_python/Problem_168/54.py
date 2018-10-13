import sys

m = {
    '^': [-1, 0],
    '>': [0, 1],
    '<': [0, -1],
    'v': [1, 0]
}

dirs = m.values()

def ok(a, dir, i, j):
    while 1:
        i += dir[0]
        j += dir[1]
        if 0 <= i < len(a) and 0 <= j < len(a[0]):
            pass
        else:
            return False
        if a[i][j] != '.':
            return True


def foo(ifile):
    r, c = [int(x) for x in ifile.readline().split()]
    a = [ifile.readline().strip() for i in range(r)]
    res = 0
    for i in range(r):
        for j in range(c):
            if a[i][j] == '.':
                continue
            dir = m[a[i][j]]
            if ok(a, dir, i, j):
                continue
            ok2 = 0
            for x in dirs:
                if ok(a, x, i, j):
                    res += 1
                    ok2 = 1
                    break

            if ok2 == 0:
                return 'IMPOSSIBLE'
    return res





def main():
    ifile = sys.stdin
    n = int(ifile.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, foo(ifile))

main()

