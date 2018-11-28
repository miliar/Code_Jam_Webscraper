# 00:24

def doit(n,m,lawnr,lawnc):
	for r in xrange(n):
		ma = max(lawnr[r])

		for c in xrange(m):
			if lawnr[r][c] != ma:
				if not all(map(lambda x:x==lawnr[r][c], lawnc[c])):
					return 'NO'
	
	return 'YES'

def main():
	# fp = open('b.in')
	fp = open('B-small-attempt0.in')

	for case in xrange(int(fp.readline())):
		n,m = map(int, fp.readline().split())

		lawnr = []
		lawnc = []

		for x in xrange(m):
			lawnc.append([])

		for x in xrange(n):
			lawnr.append(map(int, fp.readline().split()))
			for i, h in enumerate(lawnr[-1]):
				lawnc[i].append(h)

		result = doit(n,m,lawnr,lawnc)

		print 'Case #{0}: {1}'.format(case+1, result)

		# break
		# if case >= 1:
		# 	break

if __name__ == "__main__":
	main()
