def recycled_pairs(A, B):
	ans = 0
	for a0 in xrange(A, B):
		s0 = str(a0)
		a_len = len(s0)
		h0 = {}
		for i in range(1, a_len):
			b0 = int(s0[-i:] + s0[0:a_len-i])
			if len(str(b0)) == a_len and b0 > a0 and b0 <= B and b0 not in h0:
				ans += 1
				h0[b0] = 1
	
	return ans


input = open('C-small-attempt0.in')
output = open('C-small-attempt0.out', 'w')
num_of_lines = int(input.readline())
num = 0
while num < num_of_lines:
	tokens = input.readline().split()
	A = int(tokens[0])
	B = int(tokens[1])
	num_of_pairs = recycled_pairs(A, B)
	output.write('Case #' + str(num + 1) + ': ' + str(num_of_pairs) + '\n')
	num += 1
output.close()
