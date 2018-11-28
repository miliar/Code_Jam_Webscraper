for i in range(input()):
	smax, s=[x for x in raw_input().split()]
	smax=int(smax)
	s=list(s)
	tot=int(s[0])
	add=0
	for j in range(1,smax+1):
		if j>tot:
			add+=1
			tot+=int(s[j])+1
		else:
			tot+=int(s[j])

	print "Case #%d: %d" %(i+1, add)





	



