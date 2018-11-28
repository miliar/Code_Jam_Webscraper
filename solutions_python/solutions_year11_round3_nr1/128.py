from sys import stdin

def riadok():
    return map(int, stdin.readline().split())

def solve(a):
    b = [[a[y][x] for x in range(c)] for y in range(r)]
    for i in range(r):
        for j in range(c):
            if b[i][j] == '#':
                ok = True
                if i + 1 >= r or j + 1 >= c:
                    print "Impossible"
                    return
                for k in range(2):
                    for l in range(2):
                        if b[i + k][j + l] != '#':
                            print "Impossible"
                            return
                b[i][j], b[i + 1][j + 1] = '/', '/'
                b[i + 1][j], b[i][j + 1] = '\\', '\\'
    for i in range(r):
        s = str()
        for j in range(c):
            s = s + b[i][j]
        print s

for cas in range(int(stdin.readline())):
    r, c = tuple(riadok())
    a = []
    for i in range(r):
        a.append(stdin.readline().strip())
    print "Case #%d:" % (cas + 1)
    solve(a)
