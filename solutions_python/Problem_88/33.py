from sys import stdin
buf = [(l).strip() for l in stdin]
buf.reverse()

def solve():
    R, C, D = tuple(int(e) for e in buf.pop().split())
    T = [[int(j)+D for j in buf.pop()] for i in range(R)]
    WX = [[x*T[x][y] for y in range(C)] for x in range(R)]
    WY = [[y*T[x][y] for y in range(C)] for x in range(R)]
    m = 2
    for i in range(R):
        for j in range(C):
            k = max(m, 2)
            K = min(R-i, C-j)
            if k >= K:
                continue
            X = sum(WX[i+x][j+y] for y in range(k) for x in range(k) if not(x in [0, k-1] and y in [0, k-1]))
            Y = sum(WY[i+x][j+y] for y in range(k) for x in range(k) if not(x in [0, k-1] and y in [0, k-1]))
            W = sum(T[i+x][j+y] for y in range(k) for x in range(k) if not(x in [0, k-1] and y in [0, k-1]))
            while k < K:
                X += WX[i][j+k-1] + WX[i+k-1][j] + WX[i+k-1][j+k-1] + sum(WX[i+r][j+k]+WX[i+k][j+r] for r in range(1, k))
                Y += WY[i][j+k-1] + WY[i+k-1][j] + WY[i+k-1][j+k-1] + sum(WY[i+r][j+k]+WY[i+k][j+r] for r in range(1, k))
                W += T[i][j+k-1] + T[i+k-1][j] + T[i+k-1][j+k-1] + sum(T[i+r][j+k]+T[i+k][j+r] for r in range(1, k))
                if (2*i+k)*W == 2*X and (2*j+k)*W == 2*Y:
                    m = max(m, k+1)
                k += 1
    if m < 3:
        return 'IMPOSSIBLE'
    return m

T = int(buf.pop())
for i in range(T):
    print 'Case #%d:' % (i+1), solve()
