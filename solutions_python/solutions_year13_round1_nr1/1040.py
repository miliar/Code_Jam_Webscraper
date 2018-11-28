import sys
import math

input = open(sys.argv[1], 'r')

n = input.readline()
n = n[:-1]
n = int(n)

for i in range(0, n):
	line = input.readline()
	tokens = line.split()
	r = int(tokens[0])
	t = int(tokens[1])

	t -= (2 * r) + 1
	rings = 0
	
	while (t >= 0):
		t -= (2 * r) + 5
		rings += 1
		r += 2

	sys.stdout.write('Case #' + str(i + 1) + ': ' + str(rings))
	
	if (i + 1 < n):
		print('')

input.close()