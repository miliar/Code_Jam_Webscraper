tn = int(input())

dx = [-1, 0, 1, 1, 1, 0, -1, -1]
dy = [1, 1, 1, 0, -1, -1, -1, 0]

def makemap(a):
    b = [[0 for i in range(c)] for i in range(r)]
    for i in range(r):
        for j in range(c):
            if a[i][j]:
                b[i][j] = -1
            else:
                t = 0
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < r and 0 <= nj < c and a[ni][nj]:
                        t += 1
                b[i][j] = t
    return b

def dfs(x, y):
    u[x][y] = True
    res = 1
    if b[x][y] == 0:
        for k in range(8):
            ni = x + dx[k]
            nj = y + dy[k]
            if 0 <= ni < r and 0 <= nj < c and b[ni][nj] != -1 and not u[ni][nj]:
                res += dfs(ni, nj)
    return res

def check(total):
    global a, b, u, ans
    b = makemap(a)
    for i in range(r):
        for j in range(c):
            if b[i][j] != -1:
                u = [[False for i in range(c)] for i in range(r)]
                if dfs(i, j) == total:
                    a[i][j] = 2
                    ans = a
                    return True

    return False

def gen(x, y, pl, m):
    global a, r, c
    if x == r:
        return check(free)

    if y == c:
        return gen(x + 1, 0, pl, m)
    if pl > m:
        a[x][y] = False
        t = gen(x, y + 1, pl - 1, m)
        if t:
            return True
    a[x][y] = True
    return gen(x, y + 1, pl - 1, m - 1)

for test in range(1, tn + 1):
    r, c, m = map(int, input().split())
    a = [[False for i in range(c)] for i in range(r)]
    ans = None
    free = c * r - m
    gen(0, 0, c * r, m)
    print("Case #%d:" % test)
    if ans == None:
        print("Impossible")
    else:
        for i in range(r):
            for j in range(c):
                if a[i][j] == True:
                    a[i][j] = "*"
                elif a[i][j] == False:
                    a[i][j] = "."
                else:
                    a[i][j] = "c"
            print("".join(a[i]))
        
            
    

