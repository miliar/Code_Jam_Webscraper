#p3
import heapq
def solve(N, K):
    weight = {N: 1}
    pq = [-N]
    while pq:
    	node = -heapq.heappop(pq)
    	w = weight[node]
    	K -= w
    	if K <= 0:
    	    return "{} {}".format( node/2, (node-1)/2 )
    	del weight[node]
    	if node % 2:
    	    todo = [(node/2, 2 * w)]
    	else:
    	    todo = [( (node-1)/2, w ), ( node/2, w )]
    	for nei, wt in todo:
    	    if nei in weight:
    		weight[nei] += wt
    	    else:
    		weight[nei] = wt
    		heapq.heappush(pq, -nei)
    return "0 0"
    
########
fo = open('out.txt','w')
with open('in.txt','r') as fi:
    rr = lambda: fi.readline().strip()
    rrI = lambda: int(rr())
    rrM = lambda: map(int,rr().split())
    for tc in xrange(rrI()):
        zetaans = solve(*rrM())
        zeta = "Case #%i: "%(tc+1) + str(zetaans)
        print zeta
        fo.write(zeta+'\n')
fo.close()
