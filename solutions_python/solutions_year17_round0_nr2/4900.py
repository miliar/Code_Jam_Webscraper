f=open("B-small-attempt1.in","r")
#f1=f.read()
t=f.readline()
t=int(t)
f1=open("OUTPUT","w")
for i in range(t):
	n=f.readline()
	n=int(n)
	#n=input()
	flag=1
	while(flag):
		i1=n	
		i1=str(i1)
		i2=''.join(sorted(i1))
		if(i1==i2):
			f1.write("Case #"+str(i+1)+": "+str(i1)+"\n")
			flag=0
			break
		else:
			flag=1
			n=n-1
