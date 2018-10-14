infile = 'B-large.in'
outfile = 'bl.out'

def main():
	with open(infile) as f, open(outfile, 'w+') as out:
		T = int(f.readline())
		for c in range(0, T):
			N = f.readline()
			y = ltidy(str(int(N)))
			out.write('Case #{0}: {1}\n'.format(c+1, y))		

def ltidy(n):
	digs = len(n)
	l = int(n[0])
	p = l * 10 ** (digs - 1)
	alt = int(str(l - 1) + ('9' * (digs - 1)))
	print(n, p, alt)
	for dig in range(1, digs):
		d = int(n[dig])
		if d < l:
			return alt
		elif d == l:
			p = p + (d * 10 ** (digs - dig - 1))
		elif d > l:
			alt = p + int(str(d -1) + ('9' * (digs - dig - 1)))
			p = p + d * 10 ** (digs - dig - 1)
			l = d
			
	return p

if __name__=='__main__':
	main()
