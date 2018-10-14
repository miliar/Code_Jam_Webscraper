def gcd(a, b):
	if 0==a:
		return b
	if 0==b:
		return a
	if a>b:
		c = a
		a = b
		b = c
	c = a % b
	while c>0:
		a = b
		b = c
		c = a % b
	return b

def main():
	c = int(raw_input())
	case = 1;
	while case<=c:
		l = raw_input().split()
		n = int(l[0])
		R = long(l[1])
		sub = [abs(long(l[p+1])-long(l[q+1])) for p in range(n) for q in range(n) if p<q]
		ret = 0L;
		i = 0
		n = len(sub)
		while i<n:
			a = sub[i]
			b = ret
			ret = gcd(a, b)
			i += 1
		R = R % ret
		if R==0: 
			ret = 0
		else:
			ret = ret - R
		print 'Case #%d: %d' % (case, ret)
		case += 1

if __name__ == '__main__':
	main()

