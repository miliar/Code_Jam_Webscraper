import sys

def getRow(f, rn):
	r=[]
	for i in range(0,4):
		l = f.readline()
		if i+1 == rn:
			r = [int(x) for x in l.split()]

	return r

def main():
	fIn = sys.argv[1]

	with open(fIn, 'r') as f:
		T = int(f.readline())

		i = 0

		while T>=1:
			i = i+1
			n1 = int(f.readline())
			r1 = getRow(f, n1)

			n2 = int(f.readline())
			r2 = getRow(f, n2)

			c = [x for x in r1 if x in r2]

			if len(c)==0:
				print "Case #%d: Volunteer cheated!" % i
			elif len(c)==1:
				print "Case #%d: %d" % (i, c[0])
			else:
				print "Case #%d: Bad magician!" % i

			T = T-1

if __name__ == '__main__':
	sys.exit(main())
