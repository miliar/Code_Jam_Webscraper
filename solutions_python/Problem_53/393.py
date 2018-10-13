fname="A-large"
inf=open(fname+".in")
out=open(fname+".out",'w')
for case in range(1,int(inf.readline())+1):
	n,k=map(int,inf.readline().split())
	out.write("Case #%d: %s\n"%(case,all([(k/2**i)%2==1 for i in range(n)]) and "ON" or "OFF"))
