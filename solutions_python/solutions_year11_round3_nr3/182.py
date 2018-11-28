def can_play(j, P):
	for p in P:
		if j % p != 0 and p % j != 0:
			return False
	return True

f = open('in', 'r')

T = int(f.readline()[:-1])
for case_no in range(1, T + 1):
	N, L, H = map(int, f.readline()[:-1].split(' '))
	P = map(int, f.readline()[:-1].split(' '))
	J = H + 1
	for j in range(L, H + 1):
		if can_play(j, P):
			J = j
			break
	if J != H + 1:		
		print "Case #%s: %s" % (case_no, J)
	else:
		print "Case #%s: %s" % (case_no, 'NO')
