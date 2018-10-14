for queries in range(input()):
	smax,s=map(str, raw_input().split())
	smax=int(smax)
	count_of_standing=int(s[0])
	req=0
	for c in range(1,smax+1):
		if(c>count_of_standing):req+=(c-count_of_standing)
		count_of_standing+=int(s[c])+(c>count_of_standing)*(c-count_of_standing)
		#print c, count_of_standing
	print "Case #"+str(queries+1)+": "+str(req)
	
	
	