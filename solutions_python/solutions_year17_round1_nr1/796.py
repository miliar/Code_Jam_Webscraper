def solve():
    r,c = [int(v) for v in input().split()]
    g = []
    for i in range(r):
        g.append(list(input()))
    s = set()
    for i in range(r):
        for j in range(c):
            if g[i][j] != '?':
                s.add(g[i][j])
    s = list(s)
    m = {}
    for a in s:
        m[a] = [26,-1,26,-1]
    for i in range(r):
        for j in range(c):
            a = g[i][j]
            if a != '?':
                m[a][0] = min(m[a][0], i)
                m[a][1] = max(m[a][1], i)
                m[a][2] = min(m[a][2], j)
                m[a][3] = max(m[a][3], j)
    arr = [0 for i in range(len(s) * 4)]
    for i in range(len(s)):
        arr[4*i+0] = m[s[i]][0]
        arr[4*i+1] = m[s[i]][1]
        arr[4*i+2] = m[s[i]][2]
        arr[4*i+3] = m[s[i]][3]
    for i in range(len(s)):
        for a in range(arr[4*i+0], arr[4*i+1]+1):
            for b in range(arr[4*i+2], arr[4*i+3]+1):
                g[a][b] = s[i]
    return opt(r,c,g,arr,0,0,s)

def opt(r,c,g,arr,k,kk,s):
    if k == len(s):
        plot(g)
        return True
    carr = list(arr)
    cg = [list(l) for l in g]
    if kk%4==0:
        if arr[4*k+kk] > 0:
            if isempty(carr[4*k]-1, carr[4*k]-1, carr[4*k+2], carr[4*k+3],cg):
                draw(cg,carr[4*k]-1, carr[4*k]-1, carr[4*k+2], carr[4*k+3],s[k])
                carr[4*k+kk] -= 1
                if opt(r,c,cg,carr,k,kk,s):
                    return True
                else:
                    carr[4*k+kk] += 1
                    draw(cg,carr[4*k]-1, carr[4*k]-1, carr[4*k+2], carr[4*k+3],'?')
        return opt(r,c,cg,carr,k,kk+1,s)
    if kk%4==1:
        if arr[4*k+kk] < r-1:
            if isempty(carr[4*k+1]+1, carr[4*k+1]+1, carr[4*k+2], carr[4*k+3],cg):
                draw(cg,carr[4*k+1]+1, carr[4*k+1]+1, carr[4*k+2], carr[4*k+3],s[k])
                carr[4*k+kk] += 1
                if opt(r,c,cg,carr,k,kk,s):
                    return True
                else:
                    carr[4*k+kk] -= 1
                    draw(cg,carr[4*k+1]+1, carr[4*k+1]+1, carr[4*k+2], carr[4*k+3],'?')
        return opt(r,c,cg,carr,k,kk+1,s)
    if kk%4==2:
        if arr[4*k+kk] > 0:
            if isempty(carr[4*k+0], carr[4*k+1], carr[4*k+2]-1, carr[4*k+2]-1,cg):
                draw(cg,carr[4*k+0], carr[4*k+1], carr[4*k+2]-1, carr[4*k+2]-1,s[k])
                carr[4*k+kk] -= 1
                if opt(r,c,cg,carr,k,kk,s):
                    return True
                else:
                    carr[4*k+kk] += 1
                    draw(cg,carr[4*k+0], carr[4*k+1], carr[4*k+2]-1, carr[4*k+2]-1,'?')
        return opt(r,c,cg,carr,k,kk+1,s)
    if kk%4==3:
        if arr[4*k+kk] < c-1:
            if isempty(carr[4*k+0], carr[4*k+1], carr[4*k+3]+1, carr[4*k+3]+1,cg):
                draw(cg,carr[4*k+0], carr[4*k+1], carr[4*k+3]+1, carr[4*k+3]+1,s[k])
                carr[4*k+kk] += 1
                if opt(r,c,cg,carr,k,kk,s):
                    return True
                else:
                    carr[4*k+kk] -= 1
                    draw(cg,carr[4*k+0], carr[4*k+1], carr[4*k+3]+1, carr[4*k+3]+1,'?')
        return opt(r,c,cg,carr,k+1,0,s)
    return False
        
        
def draw(g,x1,x2,y1,y2,c):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if c != '?' and g[i][j] != '?':
                plot(g)
                print(x1,x2,y1,y2,c)
                print('err')
            g[i][j] = c

def isempty(x1,x2,y1,y2,g):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if g[i][j] != '?':
                return False
    return True

def plot(g):
    print('\n'.join(''.join(c for c in l) for l in g))

T = int(input())
for t in range(1, T + 1):
    print('Case #%d:' % t)
    solve()


