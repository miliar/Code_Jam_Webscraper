import bisect
pow2=[1]
for i in range(1,70):
	pow2.append(pow2[i-1]*2)
	
def mnls(n,k):
    nxt=pow2[bisect.bisect_right(pow2,k)]
    inc=nxt
    frst=nxt+k
    return ((n-frst)/inc)+1

def mxls(n,k):
    nxt=pow2[bisect.bisect_right(pow2,k)]
    prev=nxt/2
    inc=nxt
    frst=nxt+k-prev
    return ((n-frst)/inc)+1

t=int(raw_input())
for ii in range(t):
    n,k=[int(x) for x in raw_input().split()]
    print "Case #"+str(ii+1)+": "+str(mxls(n,k))+" "+str(mnls(n,k))
