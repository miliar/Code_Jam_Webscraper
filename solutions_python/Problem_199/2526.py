T=int(raw_input().strip())
for _ in xrange(T):
	print "Case #"+str(_+1)+":",
	arr,m=raw_input().strip().split()
	string=[(0 if st=='+' else 1) for st in arr]
	m,count=int(m),0
	for i in xrange(len(string)-m+1):
		if string[i]:
			count+=1
			for j in xrange(i,i+m):
				string[j]=(string[j]+1)%2
	while i<len(string):
		if string[i]!=0:
			print "IMPOSSIBLE"
			break
		i+=1
	else:
		print count
