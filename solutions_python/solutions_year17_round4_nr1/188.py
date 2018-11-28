#!/usr/bin/env python2

maxN = 101
dp3 = [[0 for i in range(maxN)] for j in range(maxN)]
dp4 = [[[0 for i in range(maxN)] for j in range(maxN)] for k in range(maxN)]

for i in range(maxN):
    for j in range(maxN):
        best = 0
        if i - 1 >= 0:
            is_one = (1 if (2 * (i - 1) + j) % 3 == 0 else 0)
            best = max(dp3[i - 1][j] + is_one, best)
        if j - 1 >= 0:
            is_one = (1 if (2 * i + j - 1) % 3 == 0 else 0)
            best = max(dp3[i][j - 1] + is_one, best)
        dp3[i][j] = best


def calc4(a, b, c):
    return 1 if (3 * a + 2 * b + c) % 4 == 0 else 0


for i in range(maxN):
    for j in range(maxN):
        for k in range(maxN):
            best = 0
            if i - 1 >= 0:
                is_one = calc4(i - 1, j, k)
                best = max(dp4[i - 1][j][k] + is_one, best)
            if j - 1 >= 0:
                is_one = calc4(i, j - 1, k)
                best = max(dp4[i][j - 1][k] + is_one, best)
            if k - 1 >= 0:
                is_one = calc4(i, j, k - 1)
                best = max(dp4[i][j][k - 1] + is_one, best)
            dp4[i][j][k] = best

def get(counts):
    answer = 0
    answer += counts[0]
    if len(counts) == 2:
        answer += (counts[1] + 1) // 2
    elif len(counts) == 3:
        answer += dp3[counts[1]][counts[2]]
    elif len(counts) == 4:
        a, b, c = counts[1:]
        answer += dp4[a][b][c]
    else:
        assert(False)
    return answer
    

T = int(input())

for case in range(1, T + 1):
    answer = 0
    N, P = map(int, input().split())
    G = [int(x) % P for x in input().split()]
    counts = []
    for i in range(P):
        counts.append(G.count(i))
    answer = get(counts)
    print("Case #", case, ": ", answer, sep='')

