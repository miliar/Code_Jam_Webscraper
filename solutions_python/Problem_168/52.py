T = input()
for ttt in range(1, T+1):
    N, M = map(int, raw_input().split())
    m = []
    for i in range(N):
        m.append(raw_input().strip())

    ans = 0

    def go(y, x, dy, dx):
        y += dy
        x += dx
        while 0 <= y < N and 0 <= x < M:
            if m[y][x] != '.':
                return True
            y += dy
            x += dx
        return False

    for i in range(N):
        for j in range(M):
            if m[i][j] == '.':
                continue

            left = go(i, j, 0, -1)
            right = go(i, j, 0, 1)
            up = go(i, j, -1, 0)
            down = go(i, j, 1, 0)

            if not (left or right or up or down):
                ans = 'IMPOSSIBLE'
                break

            if (m[i][j] == '<' and left) or (m[i][j] == '>' and right) or (m[i][j] == 'v' and down) or (m[i][j] == '^' and up):
                continue
            else:
                ans += 1
        else:
            continue
        break

    print 'Case #{}: {}'.format(ttt, ans)
