import math, collections, copy, sys
f = open('input.in','r')
g = open('output.txt','w')
"""

"""
for index in xrange(1, int(f.readline()[:-1]) + 1):
    N, K = [int(x) for x in f.readline()[:-1].split(' ')]
    Data = [0]*N
    for i in xrange(N):
        Data[i] = [int(x) for x in f.readline()[:-1].split(' ')]   # R[i], H[i]
    Data.sort(key = lambda d:(d[0], -d[0]*d[1]), reverse = True)
    for i in xrange(N):
        Data[i].append(i)
    Data_side = sorted(Data, key = lambda d:d[0]*d[1], reverse = True)
    Select = sorted(Data_side[:K], key = lambda d:(d[0], -d[0]*d[1]), reverse = True)
    D = Select[0]
    L = Data_side[K-1]
    i = D[2]
    if i == 0:
        result = math.pi*( D[0]**2 + 2*sum(d[0]*d[1] for d in Data_side[:K]))
    else:
        E = max(Data[:i], key = lambda d:d[0]*(2*d[1]+d[0]))
        if D == L:
            if K == 1:
                R = 0
            else:
                R = Select[1][0]
            if E[0]*(2*E[1]+E[0]) > D[0]*(2*D[1]+D[0]):
                result = math.pi*( E[0]**2 + 2*sum(d[0]*d[1] for d in Data_side[:K]) - 2*D[0]*D[1] + 2*E[0]*E[1] )
            else:
                result = math.pi*( D[0]**2 + 2*sum(d[0]*d[1] for d in Data_side[:K]))
        else:
            R = D[0]
            if E[0]*(2*E[1]+E[0]) - R**2 > 2*L[0]*L[1]:
                result = math.pi*( E[0]**2 + 2*sum(d[0]*d[1] for d in Data_side[:K]) - 2*L[0]*L[1] + 2*E[0]*E[1] )
            else:
                result = math.pi*( D[0]**2 + 2*sum(d[0]*d[1] for d in Data_side[:K]))



    result = str("{:.7f}".format(result))
    g.write("Case #{}: {}\n".format(index, result))
    print "Case #{}: {}\n".format(index, result)
f.close()
g.close()