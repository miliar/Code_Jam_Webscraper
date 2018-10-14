f="A-large"
fin=open(f+".in")
fout=open(f+".out",'w')
for case in range(1,int(fin.readline())+1):
	n=int(fin.readline().strip())
	ab=[]
	for _ in range(n):
		ab.append(map(int,fin.readline().strip().split()))
	res=sum([len(filter(lambda (x,y):x<xx and y>yy,ab)) for (xx,yy) in ab])
	print "Case #%d: %s"%(case,res)
	fout.write("Case #%d: %s\n"%(case,res))
