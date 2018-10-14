def solve(R, W, L):
	#rem = W%L
	return ((W/L)*R) - 1 + L# + rem
def solveRevised(R, W, L):
	rem = W%L
	if rem != 0:
		rem = 1
	return ((W/L)*R) - 1 + L + rem

	
	

f = open("A-large.in", 'r')
#f = open("test.txt", 'r')
f2 = open("outputBattleshipLarge.txt", 'w')	
t = int(f.readline())
for i in xrange(t):
	s = "Case #" + str(i+1) + ": "
	
	n = f.readline().rstrip().split()
	R, W, L = int(n[0]), int(n[1]), int(n[2])
	ans = solveRevised(R, W, L)
	#print R,W,L
	#if ans != solveRevised(R,W,L):
	#	print "and the answer is %d and revised is %d" % (ans, solveRevised(R,W,L))
	if i == t-1:
		f2.write(s+str(ans))
	else:
		f2.write(s+str(ans)+'\n')

f.close()
f2.close()
