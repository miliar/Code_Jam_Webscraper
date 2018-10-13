import sys

f = open(sys.argv[1], 'r')
T = int(f.readline())
for case in range(0, T):
    (N, M) = [int(i) for i in f.readline().split()]
    lawn = [None for n in range(0, N)]
    for n in range(0, N):
        lawn[n] = [int(m) for m in f.readline().split()]

    row_max = [0 for n in range(N)]
    for n in range(0, N):
        row_max[n] = max(lawn[n])

    col_max = [0 for m in range(M)]
    for m in range(0, M):
        col_max[m] = max([lawn[n][m] for n in range(0, N)])

    answer = "YES"
    for n in range(0, N):
        for m in range(0, M):
            if lawn[n][m] < row_max[n] and \
               lawn[n][m] < col_max[m]:
                answer = "NO"
                break
        if answer == "NO":
            break

    print "Case #%d: %s" % (case + 1, answer)
