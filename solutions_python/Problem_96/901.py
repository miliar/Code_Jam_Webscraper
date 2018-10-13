

T = int(input())
for t in range(T):
    N, S, P, *tots = map(int,input().split())
    res = 0
    for tot in tots:
    	if tot >= P+2*max(P-1,0):
    	    res += 1
    	elif S > 0 and tot >= P+2*max(P-2,0):
    	    res += 1
    	    S -= 1
    print ("Case #%d: %d" % (t+1, res))

