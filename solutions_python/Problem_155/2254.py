t = input()
for i in xrange(t):
	a = raw_input().split()
	mx = int(a[0])
	n = []
	for j in xrange(mx+1):
		n.append(int(a[1][j]))
	
	people = 0
	need = 0
	
	for j in xrange(mx+1):
		if people >= j:
			people += n[j]
		else:
			add  = j - people
			people += add + n[j]
			need += add
	print "Case #"+str(i+1)+":",need