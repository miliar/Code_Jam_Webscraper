import os

def main():
	inputf = open("war-large.in", 'r')
	output = open("war-large-ans.txt", 'w')
	tests = int(inputf.readline())
	for i in xrange(tests):
		print "Case #%d" % (i+1)
		numBlocks = int(inputf.readline())
		normal = 0
		deceit = 0
		naomi = []
		ken = []
		naomiStrings = inputf.readline().split(" ")
		kenStrings = inputf.readline().split(" ")
		for string in naomiStrings:
			naomi.append(float(string.rstrip()))
		for string in kenStrings:
			ken.append(float(string.rstrip()))
		naomi.sort()
		ken.sort()
		# Deceitful War
		nSortD = naomi[:]
		kSortD = ken[:]
		for j in xrange(numBlocks):
			lie = nSortD[0]
			if(lie > kSortD[0]):
				deceit += 1
				nSortD.remove(lie)
				kSortD = kSortD[1:]
			else:
				nSortD.remove(lie)
				kSortD = kSortD[:-1]
		# Normal War
		for j in xrange(numBlocks):
			nonlie = naomi[0]
			if(nonlie > ken[-1]):
				normal = len(ken)
				break
			else:
				naomi.remove(nonlie)
				temp = 0
				while(ken[temp] < nonlie):
					temp += 1
				ken.remove(ken[temp])
		output.write("Case #%d: %d %d\n" % (i+1, deceit, normal))

main()
