T = int(raw_input())

def doprob():
	read = raw_input()
	read = [int(k) for k in read.split()]
	R = read[0]
	C = read[1]
	array = [list(raw_input()) for i in xrange(R)]

	count = 0

	for i in xrange(R):
		for j in xrange(C):
			# test (i,j)
			if array[i][j] == '.':
				continue
			above = 0
			below = 0
			left = 0
			right = 0
			for k in xrange(j):
				if array[i][k] != '.':
					left += 1
			for k in xrange(j+1, C):
				if array[i][k] != '.':
					right += 1
			for k in xrange(i):
				if array[k][j] != '.':
					above += 1
			for k in xrange(i+1, R):
				if array[k][j] != '.':
					below += 1
			if left+right+above+below == 0:
				return "IMPOSSIBLE"
			char = array[i][j]
			if char == 'v' and below == 0:
				count += 1
			if char == '^' and above == 0:
				count += 1
			if char == '<' and left == 0:
				count += 1
			if char == '>' and right == 0:
				count += 1

	return count

for qq in range(T):
	print "Case #" + str(qq+1) + ": " + str(doprob())