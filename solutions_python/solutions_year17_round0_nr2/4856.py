file=open("test.in","r")
n=int(file.readline())
out=open("output.txt","w")

for i in range(n):
	num=int(file.readline())
	while True:
		dn=num
		r=0
		c=num%10
		flag=True
		while dn>0:
			r=dn%10
			if	r > c:
				flag=False
				break	
			dn=dn//10
			c=r
		if flag:
			out.write("Case #"+str(i+1)+": "+str(num)+"\n")
			break
		else:
			num=num-1
