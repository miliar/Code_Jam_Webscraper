#magic
fp=open("B-large.in","r")
ptr=open("output-P2.txt","w")
num_cases=int(fp.readline())
for i in range(num_cases):
	thislist=(fp.readline()).split()
        thislist=(map(float,thislist))
        c,f,x=thislist
	time=0
	ratenow=2

	while(1):
		temp1=float(x/ratenow)
		temp2=float(c/ratenow)+float(x/(ratenow+f))
		if temp2>temp1:
			time+=float(x/ratenow)
			break
		else:
			time+=float(c/ratenow)
			ratenow=ratenow+f
        ptr.write("Case #{}: {}\n".format(i+1,time))


         
