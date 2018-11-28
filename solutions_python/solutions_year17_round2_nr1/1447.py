for _ in range(int(input())):
	d,n=input().split()
	d=int(d)
	n=int(n)
	res=0
	for j in range(n):
		p,s=input().split()
		p=int(p)
		s=int(s)
		ans=(d-p)/s
		if ans>res:
			res=ans
	print("Case #"+str(_+1)+": "+str(d/res))