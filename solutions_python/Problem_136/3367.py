
T=int(raw_input())

for k in range(1, T+1):
	
	inp=raw_input().split()

	C=float(inp[0])
	F=float(inp[1])
	X=float(inp[2])

	if X < C:
		mint=X/2
		
	else:
		i=1
		mint=X/2
		cur=float(0)
		while True:
			curs=float(0)
			for j in range(0, i):
				curs+=(1/(2+j*F))
			curs*=C
			cur=curs+X/(2+F*i)
			if(cur<mint):
				mint=cur
			else:
				break
			i+=1

	print "Case #" + str(k) + ": " + str(mint)