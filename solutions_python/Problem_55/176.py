T = int(raw_input())
for t in range(1, T+1):
    R, k, N = map(int, raw_input().split())
    G = map(int, raw_input().split())
    H = []
    i = 0
    n = 0
    hasRoll = False
    r = -1
    p = 0
    while n < R and not hasRoll:
	H.append([])
	while sum(H[n])<=k and len(H[n])<=N:
	    H[n].append(G[i%N])
	    i = i + 1
	H[n].pop()
	n = n + 1
	i = i - 1
	for j, h in enumerate(H[:-1]):
	    if h==H[:-1]:
		hasRoll = True
		r = j
		p = len(H)-j-1
		H.pop()
    s = 0
    for h in H:
	s = s + sum(h)	
    if hasRoll:
	m = R - len(H)
	if m/p>=1:
	    ps = 0
	    for h in H[r:]:
		ps = ps + h
	    s = s + ps*(m/p)
	if m%p>0:
	    for i in range(r, r+m%p):
		s = s + H[i]
    print "Case #%d: %d" % (t, s)
