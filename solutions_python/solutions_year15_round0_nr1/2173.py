outf=open("wgjkag.txt","w")
for q in range(int(input())):
	l=raw_input().split(" ")
	smax=int(l[0])
	slist=list(map(int,list(l[1])))

	numstanding=0
	extras=0
	for slevel in range(smax+1):
		if slevel<=numstanding:
			numstanding+=slist[slevel]
		else:
			extras+=(slevel-numstanding)
			numstanding=slevel+slist[slevel]
		
	outf.write("Case #%d: %d\n" %(q+1, extras))

outf.close()

