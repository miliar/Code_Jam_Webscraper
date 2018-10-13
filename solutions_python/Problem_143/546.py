import sys

input = open(sys.argv[1], 'r')

t = int(input.readline())

for case in range(1, t + 1):

	[a, b, k] = map(int, input.readline().split())
	
	winning_pairs = 0
	for a_i in range(a):
		for b_i in range(b):
			winning_pairs += ((a_i & b_i) < k)

	sys.stdout.write('Case #' + str(case) + ': ')

	sys.stdout.write(str(winning_pairs))

	if (case < t):
		print('')

input.close()
