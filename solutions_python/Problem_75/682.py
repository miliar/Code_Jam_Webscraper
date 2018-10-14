import sys
f=open(sys.argv[1])
f1=open("magicka.out", "w+")
N=int(f.readline())
for i in range(N):
	line=f.readline()
	line=line.rstrip()
	comb={}
	opp={}
	elemList=[]
	spl=line.split(" ")
	c=int(spl[0])
	d=int(spl[c+1])
	invoke=spl[c+1+d+2:]
	invoke=invoke[0]
	for j in range(c):
		co=spl[1+j]
		if not co[0] in comb:
			comb[co[0]]={}
		comb[co[0]][co[1]]=co[2]
		if not co[1] in comb:
			comb[co[1]]={}
		comb[co[1]][co[0]]=co[2]
	for j in range(d):
		op=spl[c+1+1+j]
		if not op[0] in opp:
			opp[op[0]]=[]
		opp[op[0]].append(op[1])
		if not op[1] in opp:
			opp[op[1]]=[]
		opp[op[1]].append(op[0])
	for c in invoke:
		if(len(elemList)==0):
			elemList.append(c)
		else:
			if elemList[-1] in comb:
				if c in comb[elemList[-1]]:
					elemList[-1]=comb[elemList[-1]][c]
					continue
			if c in opp:
				for co in opp[c]:
					if co in elemList:
						elemList=[]
						break
				else:
					elemList.append(c)
			else:
				elemList.append(c)
	f1.write("Case #" + str(i+1) + ": " + str(elemList).replace("\'","") + "\n")
