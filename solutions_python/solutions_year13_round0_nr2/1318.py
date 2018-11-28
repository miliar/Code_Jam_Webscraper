T = int(raw_input())
for tt in xrange(T):
    N, M = map(int, raw_input().split(' '))
    max_col = [0] * M
    max_row = [0] * N
    A = [0] * N
    for n in xrange(N):
        A[n] = [0] * M
    for n in xrange(N):
        line = map(int, raw_input().split(' '))
        for m, x in enumerate(line):
            A[n][m] = x
            max_col[m] = max(x, max_col[m])
            max_row[n] = max(x, max_row[n])
    fail = False
    if N == 1 or M == 1:
        print "Case #{0}: YES".format(tt + 1)
        continue
    for n in xrange(N):
        for m in xrange(M):
            x = A[n][m]
            if x < max_col[m] and x < max_row[n]:
                fail = True
                break
        if fail:
            break
    answer = "NO" if fail else "YES"
    print "Case #{0}: {1}".format(tt + 1, answer)
