def solve():
    n, m = map(int, input().split(" "))
    board = [list(input()) for _ in range(n)]
    idx = proc = 0
    while proc < n:
        while idx < n and board[idx] == m*["?"]:
            idx += 1
        if idx == n:
            for k in range(proc, n):
                board[k] = board[proc-1]
        else:
            # solve line
            j = p2 = 0
            while p2 < m:
                while j < m and board[idx][j] == "?":
                    j += 1
                if j == m:
                    for k in range(p2, m):
                        board[idx][k] = board[idx][p2-1]
                else:
                    for k in range(p2, j):
                        board[idx][k] = board[idx][j]
                j += 1
                p2 = j
            # copy up
            for k in range(proc, idx):
                board[k] = board[idx]
            idx += 1
        proc = idx
        
    for ln in board:
        print("".join(ln))

for i in range(int(input())):
    print(f"Case #{i+1}:")
    solve()
