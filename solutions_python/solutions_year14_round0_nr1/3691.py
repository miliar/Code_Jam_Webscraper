from sys import stdin

T = int(stdin.next())
for t in xrange(T):
	M = int(stdin.next()) - 1 
	
	pre = []
	for i in range(0,4):
		lst = list(stdin.next().split())
		pre.append(lst[:])
	
	N = int(stdin.next()) - 1
	
	pos = []
	for i in range(0,4):
		lst = list(stdin.next().split())
		pos.append(lst[:])

	cont = 0
	resp = 0
	for n in pre[M]:
		if n in pos[N]:
			cont += 1
			resp = n
			continue
	
	s = ""

	if cont == 0:
		s = "Volunteer cheated!"
	elif cont == 1:
		s += str(resp)
	else:
		s = "Bad magician!"
	
	print "Case #%d: %s" % (t+1, s)