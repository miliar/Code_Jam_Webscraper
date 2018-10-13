import sys

def getGaps(pattern):
	# print "-- INSIDE GET GAP -- "
	isStart = False
	start = -1
	end = -1
	l = 0

	max_start = -1
	max_end = -1
	max_val = -1

	for i,p in enumerate(pattern):
		if p==True and isStart==True:
			isStart = False
			# print "end ", i-1
			end_index = i-1
			# print (start_index, end_index), l

			if l>max_val:
				max_val = l
				max_start = start_index
				max_end = end_index
			l=0


		if p==False and isStart==False:
			isStart = True
			start_index = i
			# print "strat ", i

		if isStart==True:
			l += 1
		# print start, end
	# print "-- END FUN --"

	return (max_start, max_end, max_val)

def printp(pattern):
	s=""
	for i in pattern:
		s += "0" if i else "."
	print s

def getLRset(pattern, index):
	pattern[index] = False

	pos = index
	while True:
		pos -= 1
		if pos<0:
			break
		if pattern[pos]==True:
			break
	L = index-pos-1

	pos = index
	while True:
		pos += 1
		if pos>=len(pattern):
			break
		if pattern[pos]==True:
			break
	R = pos-index-1
	return (L, R)

def allocate(pattern):
	start, end, length = getGaps(pattern)
	if length%2==0:
		index = start + length//2 - 1
	else:
		index = start + length//2
	pattern[index] = True

	return pattern, index

def makeInitPattern(N):
	p = list()
	p.append(True)
	for i in range(N):
		p.append(False)
	p.append(True)

	return p

def bathroom_stalls(N, K):
	pattern = makeInitPattern(N)

	for i in range(K):
		pattern, index = allocate(pattern)
	
	return getLRset(pattern, index)

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