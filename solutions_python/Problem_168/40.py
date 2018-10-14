T = int(input())
for kase in range(T):
    R, C = map(int, input().split())
    board = [input() for _ in range(R)]
    ans = 0
    good = True
    for i in range(R):
        seen = False
        for j in range(C):
            if (not seen) and board[i][j] == '<':
                ans += 1
            if board[i][j] != '.':
                seen = True
        seen = False
        for j in range(C-1, -1, -1):
            if (not seen) and board[i][j] == '>':
                ans += 1
            if board[i][j] != '.':
                seen = True
    for j in range(C):
        seen = False
        for i in range(R):
            if (not seen) and board[i][j] == '^':
                ans += 1
            if board[i][j] != '.':
                seen = True
        seen = False
        for i in range(R-1, -1, -1):
            if (not seen) and board[i][j] == 'v':
                ans += 1
            if board[i][j] != '.':
                seen = True
    rows = [0 for _ in range(R)]
    cols = [0 for _ in range(C)]
    for i in range(R):
        for j in range(C):
            if board[i][j] != '.':
                rows[i] += 1
                cols[j] += 1
    for i in range(R):
        for j in range(C):
            if board[i][j] != '.':
                if rows[i] == 1 and cols[j] == 1:
                    good = False
    if good:
        print('Case #{}: {}'.format(kase+1, ans))
    else:
        print('Case #{}: IMPOSSIBLE'.format(kase+1))
