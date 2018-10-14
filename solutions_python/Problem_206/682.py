fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')
t = int(fin.readline())
x = []
d = 0
n = 0

def check(v):
    t = d * 1.0/v
    for i in range(n):
        now = n - i -1
        x1, x2 =x[now][0], x[now][1]
        if x2 * d < (d - x1) * v:
            return False
    return True

for i in range(t):
    g = fin.readline().split(' ')
    d = int(g[0])
    n = int(g[1])
    x = []
    for j in range(n):
        g = fin.readline().split(' ')
        x.append((int(g[0]), int(g[1])))
    x.sort(key=lambda item: item[0])
    l, r = 0, 1000000000000000000

    for u in range(1000):
        mid = (l + r) / 2.0
        if check(mid):
            l = mid
        else:
            r = mid

    fout.write('Case #%d: %.8f\n' % (i+1, l))


