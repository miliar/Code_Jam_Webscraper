t = int(raw_input())
for i in xrange(1,t+1):
	n = [x for x in raw_input().strip()]
	# print n
	l = len(n)
	change = True
	while change == True:
		change = False
		for j in range(l-1):
			if n[j] > n[j+1]:
				n[j] = str(int(n[j])-1)
				for k in range(j+1,l):
					n[k] = '9'
				change = True
	n = ''.join(n)
	print "Case #{}: {}".format(i,int(n))