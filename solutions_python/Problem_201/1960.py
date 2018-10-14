from heapq import *

def get_ls_rs(ar, i, n):
    ls,rs=0,0
    li = i-1
    ri = i+1
    while li >= 0 and ar[li] == 0:
        li -= 1
        ls += 1
    while ri < n and ar[ri] == 0:
        ri += 1
        rs += 1
    return ls,rs

T = input()
for _ in xrange(T):
    N,K = raw_input().split(' ')
    N = int(N)
    K = int(K)
    ar = [1] + [0]*N + [1]
    h = [(-1*N, 1)]
    heapify(h)
    for i in xrange(K-1):
        target = -1
        mins = -1
        maxs = 100000
        # print h
        cs = heappop(h)
        # print cs
        l = cs[0] * -1
        if l == 2:
            ns = (-1, cs[1]+1)
            heappush(h, ns)
        else:
            if l % 2 == 1:
                ns1 = (-1*(l/2), cs[1])
                ns2 = (-1*(l/2), cs[1]+1+l/2)
                heappush(h, ns1)
                heappush(h, ns2)
            else:
                ns1 = (-1*(l/2 - 1), cs[1])
                ns2 = (-1*(l/2), cs[1]+l/2)
                heappush(h, ns1)
                heappush(h, ns2)
    cs = heappop(h)
    # print cs
    l = -1*cs[0]
    maxs,mins = 0,0
    if l:
        if l%2:
            maxs,mins = l/2,l/2
        else:
            maxs,mins = l/2,(l-1)/2
    print "Case #%s: %s %s" % (_+1, maxs,mins)