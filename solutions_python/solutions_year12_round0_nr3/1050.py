import sys

def main():

	fIn = sys.argv[1]

	with open(fIn, 'r') as f:
		garbage = f.readline() # Throw away the first line
		i=0
		for line in f:
			i = i+1
			a = int(line.strip().split(' ')[0])
			b = int(line.strip().split(' ')[1])

			s = 0
			for j in range(a,b+1):
				m = str(j)
				d = dict({})
				for k in range(0,len(m)):
					n = m[k:]+m[:k]
					if j<int(n) and int(n)<=b:
						d[n] = 1
				s = s+len(d)

			print 'Case #%d: %d' % (i,s)

if __name__ == '__main__':
	sys.exit(main())
