def leaf(x, y, m, M):

    def in_range(x, y):
        return 0 <= x < len(M) and 0 <= y < len(M[x])

    while True:
        x += m[0]
        y += m[1]
        if not in_range(x, y):
            return True
        if M[x][y] != '.':
            return False

def solve(M):
    moves = {
        '^': (-1, 0),
        '>': (0, 1),
        'v': (1, 0),
        '<': (0, -1)
    }
    res = 0
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != '.':
                if leaf(i, j, moves[M[i][j]], M):
                    res += 1
                if all(leaf(i, j, m, M) for m in moves.values()):
                    return 'IMPOSSIBLE'
    return res

n = int(input())
answer = 'Case #{}: {}'
for i in range(n):
    r, c = map(int, input().split())
    M = []
    for j in range(r):
        L = list(input().strip())
        M.append(L)
    print(answer.format(i + 1, solve(M)))
