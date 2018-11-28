t=input()
m=1
di={'-':'+','+':'-'}
while m<=t:
	count=0
	h=raw_input().split()
	#print h
	h[0]=list(h[0])
	h[1]=int(h[1])
	fl=0
	for i in xrange(len(h[0])):
		for j in xrange(len(h[0])):
			if h[0][j]=="-":
				if j+h[1]<=len(h[0]):
					for k in xrange(j,j+h[1]):
						h[0][k]=di[h[0][k]]
				count+=1
				break
			if h[0].count('+')==len(h[0]):
				fl=1
				break
	if fl:
		print "Case #"+str(m)+":",count
	else:
		print "Case #"+str(m)+": IMPOSSIBLE"
	m+=1