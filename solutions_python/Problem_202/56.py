#!/usr/bin/env python

fin = open("4.in", "r")
fout = open("4.out", "w")

def intersect(i, j, N):
    # determine if the lines x+y=i and x-y=j intersect in grid [0,N-1] ^ 2
    if (i - j) % 2 != 0:
        return False
    x = (i + j) / 2
    y = (i - j) / 2
    if x < 0 or x > N - 1:
        return False
    if y < 0 or y > N - 1:
        return False
    return True

T = int(fin.readline())
for t in range(T):
    print t+1
    N, M = map(int, fin.readline().split())
    rows = [False for i in range(N)]
    cols = [False for i in range(N)]
    udiags = [False for i in range(2 * N - 1)] # diags x + y = k
    ddiags = [False for i in range(2 * N - 1)] # diags x - y = k - N + 1
    grid = [[' ' for i in range(N)] for j in range(N)]
    ans = 0
    for i in range(M):
        model, x, y = fin.readline().split()
        (x, y) = map(lambda t: int(t) - 1, (x, y))
        grid[x][y] = model
        if model in ['+', 'o']:
            udiags[x + y] = True
            ddiags[x - y + N - 1] = True
            ans += 1
        if model in ['x', 'o']:
            rows[x] = True
            cols[y] = True
            ans += 1

    added = [[' ' for i in range(N)] for j in range(N)]

    # Greedily assign remaining rows to columns
    for i in range(N):
        if not rows[i]:
            for j in range(N):
                if not cols[j]:
                    rows[i] = True
                    cols[j] = True
                    m = 'x'
                    if grid[i][j] == '+':
                        m = 'o'
                    added[i][j] = m
                    ans += 1
                    break


    # Greedily assign udiags to d-diags starting from the outer ones
    for i in range(N):
        # assign ddiags to i, 2N - 2 - i
        if not udiags[i]:
            for j in range(2 * N - 1):
                if not ddiags[j] and intersect(i, j - N + 1, N):
                    udiags[i] = True
                    ddiags[j] = True
                    x = (i + j - N + 1) / 2
                    y = (i - j + N - 1) / 2
                    m = '+'
                    if grid[x][y] == 'x' or added[x][y] == 'x':
                        m = 'o'
                    added[x][y] = m
                    ans += 1
                    break
        i1 = 2 * N - 2 - i
        if not udiags[i1]:
            for j in range(2 * N - 1):
                if not ddiags[j] and intersect(i1, j - N + 1, N):
                    udiags[i1] = True
                    ddiags[j] = True
                    x = (i1 + j - N + 1) / 2
                    y = (i1 - j + N - 1) / 2
                    m = '+'
                    if grid[x][y] == 'x' or added[x][y] == 'x':
                        m = 'o'
                    added[x][y] = m
                    ans += 1
                    break

    ans2 = 0
    added_out = ""
    for x in range(N):
        for y in range(N):
            m = added[x][y]
            if m != ' ':
                ans2 += 1
                added_out += m + " " + str(x+1) + " " + str(y+1) + "\n"

    fout.write("Case #" + str(t+1) + ": " + str(ans) + " " + str(ans2) + "\n")
    fout.write(added_out)
