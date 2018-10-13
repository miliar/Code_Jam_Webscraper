from sys import maxsize
t=int(input())
n=1
while n<=t:
	large=0
	i=int(input())
	for k in range(1,i+1):
		p=k
		j=1
		ndigit=p%10
		p=p//10
		while p>0:
			digit=p%10
			if ndigit==digit:
				p//=10
				continue
			if digit>ndigit:
				j=0
				break
			ndigit=digit	
			p=p//10
		if j==1:
			large=k
	print("Case #{}: {}".format(n,large))
	n+=1