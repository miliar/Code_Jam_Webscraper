import sys
import pdb

with open(sys.argv[1]) as fh:
    T = int(fh.readline())
    for t in range(T):
        M, N = map(int, fh.readline().split())
        rowmax = [0] * M
        colmax = [0] * N
        lawn = []
        for i in range(M):
            row = map(int, fh.readline().split())
            rowmax[i] = max(row)
            lawn+=row
        for j in range(N):
            colmax[j] = max(lawn[j::N])
        flag = False

        for i in range(M):
            for j in range(N):
                if lawn[j+i*N] != rowmax[i] and lawn[j+i*N] != colmax[j]:
                    flag = True
                    break
            if flag:
                break
        print "Case #{0}: {1}".format(t+1, "NO" if flag else "YES")
