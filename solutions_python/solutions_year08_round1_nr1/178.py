
# Rule : 
# if a negative exists in either of the vectors, take the max negative multiply by the min positive
#  if no negative exists, take the min of each vector and multiply by the min
#

def minpdt(v1, v2):
	v1.sort()
	v2.sort()
	pdt = 0
	for i in range(0, len(v1)):
		if min(v2) < min(v1):
			v1, v2 = v2, v1
		pdt += min(v1) * max(v2)
		v1.remove(min(v1))
		v2.remove(max(v2))
	return pdt
	
def getInput(f):
	v1str = f.readline().strip().split(' ')
	v2str = f.readline().strip().split(' ')
	return [int(i) for i in v1str], [int(j) for j in v2str]
	
if __name__ == "__main__":
	infile = open('A-large.in', 'r')
	numCases = int(infile.readline().strip())
	for i in range(0, numCases):
		numCmps = int(infile.readline().strip())
		print "Case #%s: %s" % (i + 1, minpdt(*getInput(infile)))
	