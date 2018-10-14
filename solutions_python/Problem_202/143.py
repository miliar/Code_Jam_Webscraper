# Andy Rock
# April 8, 2016
# 
# Qualification Round 2017: Problem D. 

for T in xrange(1, int(input()) + 1):
    N, M = map(int, raw_input().split())

    hori, vert = [False] * N, [False] * N
    dia1, dia2 = [False] * (2 * N - 1), [False] * (2 * N - 1)
    cros, plus = [[False] * N for _ in xrange(N)], [[False] * N for _ in xrange(N)]

    for _ in xrange(M):
        v, R, C = raw_input().split()
        R, C = int(R) - 1, int(C) - 1

        if v != '+':
            cros[R][C] = hori[R] = vert[C] = True
        if v != 'x':
            plus[R][C] = dia1[R + C] = dia2[R - C + N - 1] = True

    add = [[False] * N for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(N):
            if not cros[i][j] and not hori[i] and not vert[j]:
                add[i][j] = cros[i][j] = hori[i] = vert[j] = True
            if not plus[i][j] and not dia1[i + j] and not dia2[i - j + N - 1]:
                if i in (0, N - 1) or j in (0, N - 1):
                    add[i][j] = plus[i][j] = dia1[i + j] = dia2[i - j + N - 1] = True

    print 'Case #%d: %d %d' % (T, sum(map(sum, cros)) + sum(map(sum, plus)), sum(map(sum, add)))
    for i in xrange(N):
        for j in xrange(N):
            if add[i][j]:
                print [['.', '+'], ['x', 'o']][cros[i][j]][plus[i][j]], i + 1, j + 1
