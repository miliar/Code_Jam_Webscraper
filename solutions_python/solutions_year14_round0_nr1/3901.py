def magician():
	g=open("output.txt", 'w')
	f=open("sample.txt", 'r')
	t=int(f.readline().rstrip())
	for i in xrange(t):
		row1=int(f.readline().rstrip())
		a=1
		while a<row1:
			f.readline()
			a+=1
		set1=list(f.readline().split(' '))
		set1[3]=set1[3].rstrip()
		while a<4:
			f.readline()
			a+=1
		row2=int(f.readline().rstrip())
		a=1
		while a<row2:
			f.readline()
			a+=1
		set2=list(f.readline().split(' '))
		set2[3]=set2[3].rstrip()
		while a<4:
			f.readline()
			a+=1
		total=list(set(set1)&set(set2))
		print total
		if len(total)==0:
			g.write("Case #"+str(i+1)+": Volunteer cheated!\n")
		if len(total)>1:
			g.write("Case #"+str(i+1)+": Bad magician!\n")
		if len(total)==1:
			g.write("Case #"+str(i+1)+": "+total[0]+"\n")


