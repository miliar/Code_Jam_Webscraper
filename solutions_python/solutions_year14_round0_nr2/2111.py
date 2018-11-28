import sys

def main():
	fIn = sys.argv[1]

	with open(fIn, 'r') as f:
		T = int(f.readline())

		i=0
		while i<T:

			r = 2.0
			(C, F, X) = [float(x) for x in f.readline().split()]

			s = 0.0
			t = X/r
			oldT = t
			
			while t<=oldT:
				u = C/r
				v = X/r
				oldT = t
				t = s+v
				s = s+u
				#print "%f %f" % (oldT, t)
				r = r+F

			print "Case #%d: %1.7f" % (i+1, oldT)

			i = i+1

if __name__ == '__main__':
	sys.exit(main())
