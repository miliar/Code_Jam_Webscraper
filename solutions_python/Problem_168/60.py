t = input()
a, s = [], []
n = m = 0

def ok(x, y):
    global n, m, a, s
    #print x, y
    #print a
    if not a[x][y]:
        return True
    dir = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    dx = dir[a[x][y]][0]
    dy = dir[a[x][y]][1]
    #print x, y, 'dir', dir[a[x][y]]
    while True:
        x += dx
        y += dy
        #print x, y
        if x < 0 or x >= n or y < 0 or y >= m:
            return False
        if a[x][y]:
            return True

def work(cs):
    global n, m, a, s, t
    a = []
    for i in range(n):
        a.append([])
        for j in range(m):
            for k in range(5):
                if s[i][j] == '.^v<>'[k]:
                    a[i].append(k)
                    break
    ans = 0
    #print a
    for i in range(n):
        for j in range(m):
            #print i, j, ok(i, j)
            if not ok(i, j):
                #print i, j, 'not ok...'
                flag = False
                for k in range(1, 5):
                    a[i][j] = k
                    if ok(i, j):
                        #print i, j, 'ok...@', k
                        flag = True
                        break
                if not flag:
                    print 'Case #' + str(cs) + ': IMPOSSIBLE'
                    return
                ans += 1
    print 'Case #' + str(cs) + ': ' + str(ans)

for cs in range(1, t + 1):
    n, m = map(int, raw_input().split())
    #print n, m
    s = []
    for i in range(n):
        s.append(raw_input())
    work(cs)

