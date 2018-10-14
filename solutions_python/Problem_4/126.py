import sys

def main(filename):
	inputFile = open(filename)
	cases = int(inputFile.readline().strip())
	results = []
	for case in range(cases):
		vectorSize = int(inputFile.readline().strip())
		v1 = []
		v2 = []
		product = 0
		for n in inputFile.readline().strip().split():
			v1.append(int(n))
		for n in inputFile.readline().strip().split():
			v2.append(int(n))
		v1.sort()
		v2.sort(reverse=True)
		if len(v1) != len(v2):
			print "vectors are unequal size, this shouldn't happen"
		for i in range(len(v1)):
			product += v1[i] * v2[i]
		results.append((case, product))
	inputFile.close()
	return results

if __name__ == "__main__":
	results = main(sys.argv[1])
	for r in results:
		print 'Case #' + str(r[0]+1) + ': ' + str(r[1])
