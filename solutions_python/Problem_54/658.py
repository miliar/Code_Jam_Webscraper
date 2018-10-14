c = int(raw_input())
case = 1;

def gcd(a,b):
	while b:
		r = a % b
		a = b
		b = r
	return a
	
while c-case+1:
	inp = raw_input().split(' ')
	n = int(inp[0])
	num = []
	for i in range(0,n):
		num.append(int(inp[i+1]))
		
	num.sort();
	
	g = 0
	
	for i in range(1,n):
		g = gcd(g, abs(num[i]-num[0]))
		
	print 'Case #%i: %i' % (case, (g-num[0]%g)%g)
	case = case+1