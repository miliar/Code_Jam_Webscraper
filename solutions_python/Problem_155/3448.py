f=open(r"A-small-attempt2.in","r")
fo=open(r'outputfile.out',"w")
l1={}

T=int(f.readline())
for i in range(T):
	standing=0
	needed=0
	l1=f.readline().split()
	D,string=l1
	D=int(D)
	string=list(string)
	##print("d: "+str(D)+"sring = "+str(string))
	for x in string:
		if int(x) > 0:
		##	print("index : "+str(string.index(x))+"standing = "+str(standing))
			if(string.index(x)>standing):
				needed=needed+string.index(x)-standing
				standing=standing+needed
		##		print("needed = "+str(needed))
			standing=standing+int(x)
		string[int(string.index(x))]='-1'
	fo.write("Case #"+str(int(i+1))+": "+str(needed)+"\n")
fo.close()
					

