import itertools
num_tests = int(raw_input())
output = ""
for i in range(num_tests):
	num_candies = int(raw_input())
	candies = raw_input().rsplit(' ')
	# first check if there is a solution
	xor = 0
	for j in range(len(candies)):
		curr = int(candies[j])
		xor^=curr
	if xor != 0:
		output += "Case #" + str(i+1) + ": NO\n"
		continue
	# else, need to find the max value
	mycandies = 0
	for j in range (1, num_candies/2 + 1):
		# iterate through all subsets of size j
		subsets = list(itertools.combinations(candies, j))
		for k in subsets:
			otherset = candies[:]
			subset_xor = 0
			subset_sum = 0
			otherset_xor = 0
			otherset_sum = 0
			for x in k:
				otherset.remove(x)
				subset_xor^=int(x)
				subset_sum += int(x)
			for x in otherset:
				otherset_xor^=int(x)
				otherset_sum += int(x)
			if otherset_xor == subset_xor:
				mycandies = max(mycandies, max(otherset_sum, subset_sum))
	output += "Case #" + str(i+1) + ": " + str(mycandies) + "\n"

print output
