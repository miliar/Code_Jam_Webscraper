T=int(input())
for i in range(1,T+1):
	f=int(input())
	for j in range(1,5):
		temp=raw_input()
		if j==f:
			fa=temp.split()
	s=int(input())
        for j in range(1,5):
                temp=raw_input()
                if j==s:
                        sa=temp.split()
	out=filter(lambda x : x in sa , fa)
	if len(out)==1:
		print "Case #%i: %s"%(i,out[0])
	elif len(out)> 0:
		print "Case #%i: Bad magician!" % i
	else:
		print "Case #%i: Volunteer cheated!" %i

