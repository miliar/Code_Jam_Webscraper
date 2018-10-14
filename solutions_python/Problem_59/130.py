for c in xrange(int(raw_input())):
	n,m=map(int,raw_input().split())
	has={"/":True}
	for i in xrange(n):
		has[raw_input()]=True
	count=0
	for i in xrange(m):
		st=raw_input()
		j=st.find("/",1)
		while (j>0):
			if st[:j] not in has:
				#print "Inserting",st[:j]
				count+=1
				has[st[:j]]=True
			j=st.find("/",j+1)
		if st not in has:
			#print "Inserting",st
			count+=1
			has[st]=True
	print "Case #"+str(c+1)+":",count
