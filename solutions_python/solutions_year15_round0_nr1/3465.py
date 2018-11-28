f=open(r"A-small-attempt0.in","r")
fo=open(r'outputfile.out',"w")
l1={}

N=int(f.readline())
for i in range(N):
	standing=0
	needed=0
	l1=f.readline().split()
	Z,string=l1
	Z=int(Z)
	string=list(string)
	for s in string:
		if int(s) > 0:
			if(string.index(s)>standing):
				needed=needed+string.index(s)-standing
				standing=standing+needed
			standing=standing+int(s)
		string[int(string.index(s))]='-1'
	fo.write("Case #"+str(int(i+1))+": "+str(needed)+"\n")
fo.close()
					

