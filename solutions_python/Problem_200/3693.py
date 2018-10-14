T=int(input())
for I in range(T):
	N=int(input())
	while True:
		s=str(N)
		lit=0
		for i in s:
			if lit<=ord(i):
				lit=ord(i)
			else:
				break
		else:
			print("Case #"+str(I+1)+": "+str(N))
			break
		N-=1