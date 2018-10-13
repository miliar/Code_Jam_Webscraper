#p2
NADIR = float('-inf')

def solve(S, prev = 0):
    N = len(S)
    if N == 1: 
    	return int(S) if int(S) >= prev else NADIR
    head = int(S[0])
    tail = S[1:]
    if head < prev:
    	return NADIR
    elif head == prev:
        return 10**(N-1) * head + solve(tail, head)
    return max( 10**(N-1) * head + solve(tail, head), 
    			10**(N-1) * head - 1)
            
########
fo = open('out.txt','w')
with open('in.txt','r') as fi:
    rr = lambda: fi.readline().strip()
    rrI = lambda: int(rr())
    rrM = lambda: map(int,rr().split())
    for tc in xrange(rrI()):
        zetaans = solve(rr())
        zeta = "Case #%i: "%(tc+1) + str(zetaans)
        print zeta
        fo.write(zeta+'\n')
fo.close()
