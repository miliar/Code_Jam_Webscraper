import sys
#fp = open('test.in')
fp =sys.stdin

def solve(N,K):
    dists = {N:1}
    y,z=N/2,N/2
    for k in xrange(K):
        l = max(dists)
        if dists[l] == 1:
            dists.pop(l)
        else:
            dists[l]-=1

        y,z=l/2,l/2 if l%2!=0 else l/2-1
        if y in dists:
            dists[y] +=1
        else:
            dists[y] = 1
        if z in dists:
            dists[z] +=1
        else:
            dists[z] = 1

    return y,z

T = int(fp.readline())

for tc in xrange(T):
    N,K = (int(t) for t in fp.readline().split(' '))
    y,z = solve(N,K)
    print "Case #%d: %d %d"%(tc+1,y,z)