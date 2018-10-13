def solve():
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4
    n, m = map(int, input().split())
    A = [input() for i in range(n)]
    P = [[None for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if A[i][j] != ".":
                P[i][j] = set([UP, RIGHT, DOWN, LEFT])
    for i in range(n):
        j = 0
        while j < m and A[i][j] == ".":
            j += 1
        if j < m:
            P[i][j].discard(LEFT)
        j = m - 1
        while j >= 0 and A[i][j] == ".":
            j -= 1
        if j >= 0:
            P[i][j].discard(RIGHT)
    for j in range(m):
        i = 0
        while i < n and A[i][j] == ".":
            i += 1
        if i < n:
            P[i][j].discard(UP)
        i = n - 1
        while i >= 0 and A[i][j] == ".":
            i -= 1
        if i >= 0:
            P[i][j].discard(DOWN)
    ans = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] != ".":
                if not P[i][j]:
                    return "IMPOSSIBLE"
                if (
                    (A[i][j] == "^" and UP in P[i][j]) or
                    (A[i][j] == ">" and RIGHT in P[i][j]) or
                    (A[i][j] == "v" and DOWN in P[i][j]) or
                    (A[i][j] == "<" and LEFT in P[i][j])
                    ):
                    pass
                else:
                    ans += 1
    return ans

T = int(input())
for t in range(1, T + 1):
    print("Case #" + str(t) + ":", solve())

