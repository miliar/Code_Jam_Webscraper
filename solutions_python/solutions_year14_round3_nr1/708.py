a=[2**i for i in range(0,13)]
def gcd_Stein(a, b):    
    if a < b:
        a, b = b, a
    if (0 == b):
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd_Stein(a/2, b/2)
    if a % 2 == 0:
        return gcd_Stein(a / 2, b)
    if b % 2 == 0:
        return gcd_Stein(a, b / 2)
    
    return gcd_Stein((a + b) / 2, (a - b) / 2)

def solve(p,q):
	c=gcd_Stein(p,q)
	p=p/c
	q=q/c
	if q not in a:
		return "impossible"
	else:
		step=0
		while q>p and step<=40:
			q/=2
			step+=1
		if q>p:
			return "impossible"
		else:
			return str(step)

T=input()
for i in range(1,T+1):
	p,q=map(int,raw_input().split('/'))
	print "Case #%d: %s"%(i,solve(p,q))


