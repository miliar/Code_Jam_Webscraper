
T = int(raw_input())
for t in range(T):
	rgrid = []
	cgrid = []
	r = int(raw_input())-1
	for i in range(4):
		rgrid.append(raw_input().split())
	c = int(raw_input())-1
	for i in range(4):
		cgrid.append(raw_input().split())
			
	rset = set()
	cset = set()
	for i in range(4):
		rset.add(rgrid[r][i])
		cset.add(cgrid[c][i])
	
	answ = list(cset.intersection(rset))
	ans = ""
	if len(answ) == 0: ans = "Volunteer cheated!"
	elif len(answ) == 1: ans = answ[0]
	else: ans = "Bad magician!"
	print "Case #%d: %s"%(t+1, ans)
	
		
