import sys

# The name of the file
FILE_NAME = 'B-large'

f_in = open(FILE_NAME + '.in', 'r')
f_out = open(FILE_NAME + '.out', 'w')

# Read the number of tests
T = int(f_in.readline())

# For each test...
for t in range(T):

	# Read the N and M
	N, M = map(int, f_in.readline().split())

	lawn = list()

	# Default result
	result = "YES"

	# Read the lawn
	for i in range(N):
		lawn.append(map(int, f_in.readline().split()))

	# Transpose the matrix
	tlawn = [[lawn[i][j] for i in range(N)] for j in range(M)]

	# Check if it's possible
	for i in range(N):
		for j in range(M):
			if lawn[i][j] >= max(lawn[i]) or lawn[i][j] >= max(tlawn[j]):
				pass
			else:
				result = "NO"
				break;
		
	# Write the output
	f_out.write("Case #" + str(t + 1) + ": " + result)

	if t + 1 < T: f_out.write("\n")

f_out.close()
f_in.close()