# from collections import *
# from itertools import *
# from heapq import *


def solve_small(N, C, M, A):
    # for l in A:
    #     print l
    L = [[0 for j in range(C + 1)] for i in range(N + 1)]
    for p, b in A:
        print p, b
        L[p][b] += 1
    tickets1 = sum(L[i][1] for i in range(N + 1))
    tickets2 = sum(L[i][2] for i in range(N + 1))
    # print tickets1, tickets2, sum(L[1]), L[1][1], L[1][2], L[2][1], L[2][2]
    need = max(sum(L[1]), tickets1, tickets2)
    res = 0
    for i in range(N + 1):
        res += max(0, sum(L[i]) - need)
    return str(need) + ' ' + str(res)


def solve(N, C, M, A):
    # for l in A:
    #     print l
    L = [[0 for j in range(C + 1)] for i in range(N + 1)]
    for p, b in A:
        print p, b
        L[p][b] += 1
    need = 0
    for j in range(C + 1):
        need = max(need, sum(L[i][j] for i in range(N + 1)))
    tickets = 0
    for i in range(1, N + 1):
        tickets += sum(L[i])
        need = max(need, (tickets + i - 1) / i)
    res = 0
    for i in range(N + 1):
        res += max(0, sum(L[i]) - need)
    return str(need) + ' ' + str(res)


def main():
    T = int(fi.readline().strip())
    for i in xrange(T):
        N, C, M = map(int, fi.readline().strip().split())
        A = []
        for _ in range(M):
            A.append(map(int, fi.readline().strip().split()))
        res = solve(N, C, M, A)
        out = "Case #%d: %s\n" % (i + 1, res)
        print out
        fo.write(out)

fi = open('B-large.in', 'r')
fo = open('B-large.out', 'w')
main()
fi.close()
fo.close()
