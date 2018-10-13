import math

file_strings = []
with open("bathroom_stalls_input.txt") as data_file:
	for line in data_file:
		file_strings.append(line.strip())

T = file_strings[0] # number of testcases
file_strings.pop(0)
T = int(T)

for i in range(1, T + 1):
	N, K = file_strings.pop(0).split()[0:2]
	N = int(N)
	K = int(K)
	power = 1
	while((2 * power) - 1) < K:
		power = 2 * power
	higher = math.ceil((N - power + 1)/power)
	lower = math.floor((N - power + 1)/power)
	X = 0
	if(K - power + 1) <= ((N - power + 1) % power):
		X = higher
	else:
		X = lower

	#numArray = []
	#numArray.append(N)
	#for j in range(int(K) - 1):
	#	largest = max(numArray)
	#	numArray.pop(numArray.index(largest))
	#	largest -= 1
	#	b = math.ceil(largest/2.0)
	#	s = math.floor(largest/2.0)
	#	numArray.append(b)
	#	numArray.append(s)
	#X = max(numArray)
	#X = float(X)
	big = math.ceil((X-1.0)/2.0)
	small = math.floor((X-1.0)/2.0)

	print("Case #{}: {} {}".format(i, big, small))