infilename="C-large.in"
outfilename="C.out"

infile = open(infilename)
outfile= open(outfilename,"w")

ncases=int(infile.readline())

for casenumber in range(1,ncases+1):
	line = infile.readline()
	conf=line.split()
	A=int(conf[0])
	B=int(conf[1])
	found=0
	for n in range(A,B+1):
		ns=str(n)
		flist=[]
		for i in range(0,len(ns)):
			tr=int(ns[i:]+ns[:i])
			if tr<=B and n<tr and tr not in flist:
				found+=1
				flist.append(tr)
	outfile.writelines("Case #"+str(casenumber)+": "+str(found)+"\n")

