
def main():
	lines = open("A-small-attempt0.in").readlines()
	n = int(lines[0])
	for x in xrange(n):
		row1 = int(lines[1+10*x])
		row2 = int(lines[6+10*x])
		line1 = lines[1+10*x+row1]
		line2 = lines[6+10*x+row2]
		ints1 = [int(n) for n in line1.split()]
		ints2 = [int(n) for n in line2.split()]
		intersect = list(set(ints1) & set(ints2))
		if len(intersect) == 1:
			print "Case #{0}: {1}".format(x+1, intersect[0])
		elif len(intersect) == 0:
			print "Case #{0}: Volunteer cheated!".format(x+1)
		else:
			print "Case #{0}: Bad magician!".format(x+1)

if __name__=='__main__':
	main()
