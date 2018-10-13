# your code goes here
t=int(input())
i=1
while(i<=t):
	n =str (input())
	flag=1
	#while(n.rfind("0")!=-1):
	#	n=str(int(n)-10**(len(n)-n.rfind("0")-1))
	while(flag==1):
		l=list(n)
		if(l==sorted(l)):
			flag=0
			break
		else:
			n="".join(l)
			n=str(int(n)-1)
	print("Case #"+str(i)+": "+str(n))
	i=i+1