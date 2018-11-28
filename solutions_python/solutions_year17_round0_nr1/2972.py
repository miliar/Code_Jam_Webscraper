
fin = open("in")
fout = open("out","w")






t = int(fin.readline())
for case in range(t):
	cakes,k = fin.readline().strip().split()
	k=int(k)
	cakes = list(cakes)
	c=0
	for i in range(len(cakes)-k+1):
		if cakes[i] == "-":
			c+=1
			for j in range(k):
				cakes[i+j] = "+" if cakes[i+j] == "-" else "-"
	
	if cakes.count("-") == 0:
		fout.write("Case #"+str(case+1)+": "+str(c)+"\n")
	else:
		fout.write("Case #"+str(case+1)+": "+"IMPOSSIBLE"+"\n")


	