import sys


def flips(input, k):
	input = list(input)
	cnt = 0
	idx = 0

	while idx < len(input):
		# print idx
		if input[idx] == '-' and idx+k-1 < len(input):
			input[idx] = '+'
			for i in xrange(k-1):
				if input[idx+i+1] == '+':
					input[idx+i+1] = '-'
				else:
					input[idx+i+1] = '+'
			idx += 1		
			cnt += 1	

		else:
			idx += 1
		# print ''.join(input), ' ', idx

	for i in input[::-1]:
		if i=='-':
			return 'IMPOSSIBLE'

	return cnt

if __name__=='__main__':
	cases = -1
	cnt = 1
	file = sys.argv[1]

	with open(file) as fin:
		for line in fin:
			if cases == -1:
				cases = line
			else:
				inp = line.split(' ')
				res = flips(inp[0], int(inp[1]))
				print 'Case #%d: %s' % (cnt, res) 
				cnt += 1




