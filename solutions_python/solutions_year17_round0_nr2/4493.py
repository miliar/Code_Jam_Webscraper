t = int(raw_input())  
for i in xrange(1, t + 1):
	n = int(raw_input())
	for j in range(n,0,-1):
		s=str(j)
		#print (i,j)
		l=len(s)
		if(j%10 == 0):
			continue
		if(l==1):
  			print "Case #{}: {}".format(i,s)
			break
		for k in range(0,l-1):
		#	print (i,j,k)
			if(int(s[k])>int(s[k+1])):
				break 
		#print (i,j,k,l)
		if(k==l-2 and s[k]<=s[k+1]):
  			print "Case #{}: {}".format(i,s)
			break

