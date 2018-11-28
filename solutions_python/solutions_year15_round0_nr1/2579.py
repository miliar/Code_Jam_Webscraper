FILENAME = 'A-large.in'

inp = open(FILENAME, 'rU').readlines()
#print(inp)

T = int(inp[0])
#print(T)

output = []

for line in inp[1:]:
	S_max, num_S = line.split()
	S_max = int(S_max)
	num_S = map(int, num_S)  # (n(0), n(1), ..., n(S_max))

	clapped = 0  # people who have clapped so far
	friends = 0  # friends added
	for S, n_S in enumerate(num_S):  # shyness level, num of ppl with that shyness level
		if n_S > 0 and clapped >= S:
			clapped += n_S
		elif n_S > 0:  # clapped < S
			friends += S - clapped
			clapped = S + n_S

	output.append('Case #{}: {}'.format(len(output)+1, friends))

print(output)
with open('output.txt', 'w') as output_file:
	output_file.write('\n'.join(output))