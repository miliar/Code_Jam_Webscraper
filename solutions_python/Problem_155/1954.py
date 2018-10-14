T = int(raw_input())

for t in range(1, T+1):
    ln = raw_input().split()
    S_max = int(ln[0])
    hist = [int(ln[1][i]) for i in range(S_max+1)]
    standing = hist[0]
    add = 0
    i = 1
    while i < len(hist):
    	if i > standing:
    	    add += (i-standing)
    	    standing += (i-standing)
    	standing += hist[i]
    	i += 1
    print 'Case #%d: %d'%(t, add)
    
