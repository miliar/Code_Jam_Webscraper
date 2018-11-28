for _ in range(input()):
	s="Case #"+str(_+1)+": "
	n=input()
	c=map(int,raw_input().split())
	s+=str(sum([i+1!=c[i] for i in range(n) ]))+".000000"
	print s
