def isTidy(n):
	for i in xrange(len(n)-1):
		if n[i] > n[i+1]:
			return False
	return True

T = int(raw_input())

for i in xrange(T):
	N = raw_input()
	found = False

	while not found:
		if len(N) == 1 or isTidy(N):
			found = True
			lastn = N
		else :
			N = str(int(N)-1)

	#output
	print "Case #" + str(i+1) + ": " + lastn