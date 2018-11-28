import sys

def makeInitPattern(N):
	return list("0"+"."*N+"0")

def getLRset(pattern, index):
	# pattern = list(pattern)
	if pattern[index]=="0":
		return None

	pos = index
	while True:
		pos -= 1
		if pos<0:
			break
		if pattern[pos]=="0":
			break
	L = index-pos-1

	pos = index
	while True:
		pos += 1
		if pos>=len(pattern):
			break
		if pattern[pos]=="0":
			break
	R = pos-index-1
	return (L,R)


def allocate(pattern):
	LRSet = list()
	for i in range(len(pattern)):
		if pattern[i]!="0":
			LRSet.append(getLRset(pattern, i))
		else:
			LRSet.append((None, None))
	#print "LRSET : ", LRSet

	MinSet = list()
	for i,j in LRSet:
		MinSet.append(i if i<j else j)
	#print "MINSET : ", MinSet

	MaxSet = list()
	for i,j in LRSet:
		MaxSet.append(j if i<j else i)
	#print "MAXSET : ", MaxSet


	maxValue = max(MinSet)
	#print "MaxValue from MIN : ", maxValue
	min_count = MinSet.count(maxValue)
	if min_count == 1:
		index = MinSet.index(maxValue)
		pattern[index] = "0"
		
		return LRSet[index]

	maxValue = max(MaxSet)
	#print "MaxValue from MAX : ", maxValue
	max_count = MaxSet.count(maxValue)
	if max_count == 1:
		#TODO correct here 
		index = MinSet.index(maxValue)
		#print MinSet
		index = LRSet[index][0]+index + 1
		#print "index : ", index
		pattern[index] = "0"

		return LRSet[index]

	#go for leftmost value
	# print "min count : ", min_count, "max_count : ", max_count
	if min_count <= max_count:
		maxValue = max(MinSet)
		index = MinSet.index(maxValue)
		pattern[index] = "0"
	else:
		maxValue = max(MaxSet)
		index = MaxSet.index(maxValue)
		pattern[index] = "0"

	return LRSet[index]

def bathroom_stalls(N, K):
	pattern = makeInitPattern(N)
	for i in range(K):
		L, R = allocate(pattern)
		# print pattern
	return (L,R)

def main():
	file_in = open(sys.argv[1], "r")
	file_out = open("out", "w")

	T = int(file_in.readline())

	for testcase in range(1, T+1):
		N, K = map(int, file_in.readline().split(' '))
		if N==K:
			L,R = 0,0
		else:
			L, R = bathroom_stalls(N, K)
		out_string = "Case #%d: %d %d\n" % (testcase, R, L)
		print out_string,
		file_out.write(out_string)

if __name__ == '__main__':
	main()