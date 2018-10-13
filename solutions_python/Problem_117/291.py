tcs = int(input())

for tc in range(1, tcs+1):
    n, m = (int(i) for i in input().split(' '))

    board = [[int(i) for i in input().split(' ')] for i in range(n)]

    order = sorted(((i, j) for i in range(n) for j in range(m)), key=lambda k: board[k[0]][k[1]])

    visit = [[False] * m for i in range(n)]

    for i, j in order:
        if not visit[i][j]:
            if all(board[i][k] <= board[i][j] for k in range(m)):
                for k in range(m):
                    visit[i][k] = True
                continue
            elif all(board[k][j] <= board[i][j] for k in range(n)):
                for k in range(n):
                    visit[k][j] = True
                continue
            else:
                break

    if all(visit[i][j] for i in range(n) for j in range(m)):
        print("Case #%d: YES" % tc)
    else:
        print("Case #%d: NO" % tc)

