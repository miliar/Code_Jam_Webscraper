import heapq as hq

T = int(input())
for x in range(1, T + 1):
    N, M = map(int, input().split())
    cells = [['.' for _ in range(N)] for _ in range(N)]
    idx = -1
    lo = []
    lp = []
    lx = []
    ans = []
    pts = 0
    for i in range(M):
        Chr, R, C = input().split()
        C = int(C)
        if Chr == '+':
            lp.append(C)
            pts += 1
        elif Chr == 'x':
            Chr = 'o'
            ans.append(('o', 1, C))
            lo.append(C)
            pts += 2
        else:
            lo.append(C)
            pts += 2
        cells[0][C - 1] = Chr
    if len(lo) == 0:
        cells[0][N - 1] = 'o'
        ans.append(('o', 1, N))
        lo.append(N)
        if N in lp:
            lp.remove(N)
            pts += 1
        else:
            pts += 2

    for c in range(1, N + 1):
        if c not in lo and c not in lp:
            cells[0][c - 1] = '+'
            ans.append(('+', 1, c))
            pts += 1
    for r in range(2, N):
        c = lo[0] + r - 1
        if N < c:
            c = (c + N + 1) % N
        cells[r - 1][c - 1] = 'x'
        lx.append(c)
        ans.append(('x', r, c))
        pts += 1
    for c in range(2, N):
        cells[N - 1][c - 1] = '+'
        ans.append(('+', N, c))
        pts += 1
    if 1 not in lx and 1 not in lo:
        cells[N - 1][0] = 'x'
        ans.append(('x', N, 1))
        pts += 1
    elif N not in lx and N not in lo:
        cells[N - 1][N - 1] = 'x'
        ans.append(('x', N, N))
        pts += 1
#    for line in cells:
#        print(line)
    print("Case #%d: %d %d" % (x, pts, len(ans)))
    for Chr, r, c in ans:
        print("%s %d %d" % (Chr, r, c))
