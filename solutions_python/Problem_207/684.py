def get_next(res,cp,A):
#	print("".join(res))
	n = len(res)
	cur = res[cp]
	cp += 1
	cp = cp % n
	while ((res[cp]<>" ") or (cur==A)):
		cur = res[cp]
		cp += 1
		cp = cp % n
#		print("cp ", cp, " ", res[cp])
	return cp
	
def solve(n,a,b,c,A,B,C):
	if (a>(n//2)):
		result = "IMPOSSIBLE"
	else:
		cp = n-1
		res = [" "] * n 
		while (a>0):
			a -= 1
			cp = get_next(res,cp,A)
			res[cp] = A
		while (b>0):
			b -= 1
			cp = get_next(res,cp,B)
			res[cp] = B
		while (c>0):
			c -= 1
			cp = get_next(res,cp,C)
			res[cp] = C
		result = "".join(res)
	return(result)
			


for case in range(1, int(input())+1):
	(N,R,O,Y,G,B,V) = list(map(int,raw_input().split()))
	only1 = False
	result = ""
	r = R - G
	if (G>0 and r==0):
		only1 = True
	b = B - O
	if (O>0 and b==0):
		if only1:
			result = "IMPOSSIBLE"
		else:
			only1 = True
	y = Y - V
	if (V>0 and y==0):
		if only1:
			result = "IMPOSSIBLE"
		else:
			only1 = True
#	print("r:%d b:%d y:%d" % (r,b,y))
	if ((r<0) or (b<0) or (y<0)):
			result = "IMPOSSIBLE"
	if (result<>""):
			result = "IMPOSSIBLE"
	else:
		if only1:
			result = "RG" * R + "BO" * B + "YV" * Y
		else:
			n = N - 2 * ( G + O + V )
			if (r>b):
				if (r>y):
					if (b>y):
						result=solve(n,r,b,y,"R","B","Y")
					else:
						result=solve(n,r,y,b,"R","Y","B")
				else:
					result=solve(n,y,r,b,"Y","R","B")
			else:
				if (b>y):
					if (r>y):
						result=solve(n,b,r,y,"B","R","Y")
					else:
						result=solve(n,b,y,r,"B","Y","R")
				else:
					result=solve(n,y,b,r,"Y","B","R")
	if (result=="IMPOSSIBLE"):
		print ("Case #%d: IMPOSSIBLE" % (case))
	else:
		result = result.replace("R","R"+"GR"*G,1)
		result = result.replace("B","B"+"OB"*O,1)
		result = result.replace("Y","Y"+"VY"*V,1)		
		print ("Case #%d: %s" % (case,result))
