import sys

def main():

	fIn = sys.argv[1]

	with open(fIn, 'r') as f:
		garbage = f.readline() # Throw away the first line
		i=0
		for line in f:
			i = i+1
			l = [int(x) for x in line.strip().split(' ')]
			n = l[0]
			s = l[1]
			p = l[2]
			T = l[3:]
			G=0

			for t in T:
				if t<2:
					if t>=(p*3-2):
						G = G+1
				elif t>=(p*3-2):
					G = G+1
					#print 'Good enough! %d' % t
				elif t>=(p*3-4) and s>0:
					G = G+1
					s = s-1
					#print 'It\'s a stretch! %d' % t

			print 'Case #%d: %d' % (i,G)
			#print line.strip()

if __name__ == '__main__':
	sys.exit(main())
