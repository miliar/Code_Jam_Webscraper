f=open(r"A-small-attempt1.in","r")
fo=open(r'outputfile.out',"w")
p1={}

X=int(f.readline())
for i in range(X):
	std=0
	nd=0
	p1=f.readline().split()
	K,strg=p1
	K=int(K)
	strg=list(strg)
	for v in strg:
		if int(v) > 0:
			if(strg.index(v)>std):
				nd=nd+strg.index(v)-std
				std=std+nd
			std=std+int(v)
		strg[int(strg.index(v))]='-1'
	fo.write("Case #"+str(int(i+1))+": "+str(nd)+"\n")
fo.close()
					

