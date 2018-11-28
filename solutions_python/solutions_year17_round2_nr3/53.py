import heapq
import copy
t = int(raw_input())
maxd = 10**18

# class Graph(object):
#     def __init__(self, n):
#         self.n = n
#         self.elist = [[] for x in xrange(n)]
#     def edge(self, u, v, horse, )

for kei in xrange(t):
    n, q = (int(x) for x in raw_input().split())
    horse = []
    for i in xrange(n):
        e, s = (int(x) for x in raw_input().split())
        horse.append((e, s))
    mat = []
    for i in xrange(n):
        mat.append([maxd if x == '-1' else int(x) for x in raw_input().split()])
    for i in xrange(n):
        mat[i][i] = 0
    # print mat
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
    # print mat
    nmat = [[maxd]*n for x in xrange(n)]
    for i in xrange(n):
        nmat[i][i] = 0
    for j in xrange(n):
        e, s = horse[j]
        for k in xrange(n):
            if j == k:
                continue
            if mat[j][k] <= e:
                nmat[j][k] = min(nmat[j][k], mat[j][k] / float(s))
                    # g.edge(j, k, i, 2[j][k] / float(s))
    mat = nmat
    for k in xrange(n):
        for i in xrange(n):
            for j in xrange(n):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])
    res = []
    for i in xrange(q):
        u, v = (int(x) for x in raw_input().split())
        res.append(mat[u-1][v-1])
    sres = " ".join("%.8f" % x for x in res)
    print "Case #%d: %s" % (kei+1, sres)
