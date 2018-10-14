f=open("in.txt")
f_out=open("out.txt","w")
n=int(f.readline())
for case in range(1,n+1):
	line=f.readline().strip().split()
	ones=[line[i] for i in range(1,len(line),2)]
	twos=[line[i] for i in range(2,len(line),2)]
	pairs=zip(ones,twos)
	T=0
	tb=0
	to=0
	db=1
	do=1
	for p in pairs:
		dnow=int(p[1])
		robotnow=p[0]
		if robotnow=="B":
			T=1+max(abs(db-dnow)+tb,T)
			tb=T
			db=dnow
		else:
			T=1+max(abs(do-dnow)+to,T)
			to=T
			do=dnow
	f_out.write("Case #%s: %s\n" % (case,T))
