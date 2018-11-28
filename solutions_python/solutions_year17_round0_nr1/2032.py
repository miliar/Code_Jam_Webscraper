def pancakes(S, K):

	# translate the string into a boolean list since strings aren't mutable
	grill = []
	for cake in S:
		if cake == "-":
			grill.append(False)
		else:
			grill.append(True)

	# keep track of how many flips we do
	flips = 0

	# loop through each pancake big-flipping the negative ones
	for index, happy in enumerate(grill):

		# if we found a sad pancake, we do a big-flip (if we can)
		if not happy and (index + K) <= len(grill):
			for offset in range(K):
				grill[index + offset] = not grill[index + offset]
			flips += 1

	# check the last big-flippable range to ensure everthing is happy
	for index in range(len(grill) - K + 1, len(grill)):
		happy = grill[index]
		if not happy:
			flips = "IMPOSSIBLE"

	return flips

# play each case
num_cases = int(input())
for case_num in range(num_cases):

	# read in the current case
	S, K = input().split(" ")
	S = str(S)
	K = int(K)

	# run the current case
	print("Case #{case}: {result}".format(
		case=case_num + 1,
		result=pancakes(S, K),
	))
