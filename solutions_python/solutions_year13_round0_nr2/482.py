f=open("B-large.in","r")
g=open("write_B.out","w")

T=int(f.readline())
for t in xrange(1,T+1):
	NM=f.readline()
	NM=NM.split()

	n=int(NM[0])
	m=int(NM[1])
	tableChar=[]
	for r in xrange(n):
		line=f.readline()
		line=line.split()
		tableChar.append(line)
	tableInt=[]
	for r in xrange(n):
		l=[]
		for c in xrange(m):
			l.append(int(tableChar[r][c]))
		tableInt.append(l)
	#print tableInt

	#keep max in each row
	max_r=[]
	max_c=[]
	for r in xrange(n):
		M=0
		for c in xrange(m):
			if M<tableInt[r][c]:
				M=tableInt[r][c]
		max_r.append(M)

	#keep max in each col
	for c in xrange(m):
		M=0
		for r in xrange(n):
			if M<tableInt[r][c]:
				M=tableInt[r][c]
		max_c.append(M)

	isCorrect=True
	for c in xrange(m):
		for r in xrange(n):
			if tableInt[r][c]!=min(max_r[r],max_c[c]):
				isCorrect=False

	if isCorrect:
		w=": YES"
	else:
		w=": NO"
	g.write("Case #"+str(t)+w+'\n')
f.close()
g.close()