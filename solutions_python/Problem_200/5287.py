n=int(input())
p=list()
for i in range(n):
	l=int(input())
	p.append(l)
for i in range(0,len(p)):
	for j in range(p[i],0,-1):
		dig=list()
		n1=j
		while(n1!=0):
			d=int(n1%10)
			dig.append(d)
			n1=int(n1/10)
		dig.sort()
		num1 = int(''.join(map(str,dig)))
		if(num1==j):
			print("Case #{}: {}".format(i+1,num1))
			break
