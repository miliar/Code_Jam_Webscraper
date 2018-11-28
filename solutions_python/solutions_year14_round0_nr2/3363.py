def cpsanf(c,f,x,cps,n):
	return cps+f*n

def winanf(c,f,x,cps,n):
	return x/cpsanf(c,f,x,cps,n)

def ttbnf(c,f,x,cps,n):
	if n == 0:
		return 0
	return c/(cpsanf(c,f,x,cps,n-1))

def y(z):
	return sum

n = int(input())
for i in range(n):
	c, f, x = [float(i) for i in input().split()]
	k = 0
	while True:
		
		h = x/(2+f*k)+sum(ttbnf(c,f,x,2,n) for n in range(1, k+1))
		g = x/(2+f*(k+1))+sum(ttbnf(c,f,x,2,n) for n in range(1, k+2))
		
		if h<g:
			break
		#input()
		k+=1
	

	print('Case #{}: {}'.format(i+1, round(h,7)))

	