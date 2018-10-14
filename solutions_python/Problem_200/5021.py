n=int(raw_input())
seq=[]
for i in range(n):
    seq.append(raw_input())

for i in xrange(n):
	for j in xrange(int(seq[i]),1,-1):
		temp=map(int,str(j))
		if all(earlier<=later for earlier,later in zip(temp,temp[1:])):
			seq[i]=j
			break

for i in range(n):
    print "Case #"+str(i+1)+":"+" "+str(seq[i])
    

    
