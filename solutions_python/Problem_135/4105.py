
FIN=open("A-small-attempt0.in","r")
FOUT=open("prob1.out","w")

cases=FIN.readline()
for c in range(1,int(cases)+1):
	G=[]
	for i in range(2):
		A=FIN.readline()
		for j in range(4):
	
			l=FIN.readline()
			print l
			if j == (int(A)-1):
				G.append(l.split())
				print G[i]
			
	res=set(G[0]).intersection(G[1])
	res=list(res)

	if len(res) > 1:
		FOUT.write("Case #"+str(c)+": Bad magician!\n")
	elif len(res)==1:
		FOUT.write("Case #"+str(c)+": "+str(res[0])+"\n")
	else:
		FOUT.write("Case #"+str(c)+": Volunteer cheated!\n")

		
