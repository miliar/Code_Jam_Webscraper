
from math import ceil, floor

def out_of_inputs(packets):
	# returns whether or not one or more of the inputs have all been used up
	for ingredient in range(len(packets)):
		if len(packets[ingredient]) == 0:
			return True
	return False

numInputs = int(input())

for i in range(numInputs):
	numIngredients, numPackets = [int(num) for num in input().split(" ")]
	amountsNeeded = [int(num) for num in input().split(" ")]
	packets = []
	for ingredient in range(numIngredients):
		packetSizes = [int(num) for num in input().split(" ")]
		packetSizes = sorted(packetSizes)
		packets.append(packetSizes)
	numGroups = 0
	while not out_of_inputs(packets):
		smallestRatio = 999999999999999
		bestIngredient = None
		for ingredient in range(numIngredients):
			currRatio = float(packets[ingredient][0]) / float(amountsNeeded[ingredient])
			if currRatio < smallestRatio:
				smallestRatio = currRatio
				bestIngredient = ingredient
		smallestNumRecipies = ceil(smallestRatio / 1.1)
		largestNumRecipies = floor(smallestRatio / .9)
		if largestNumRecipies < smallestNumRecipies:
			# means that the current smallest ratio ingredient can't be made into anything, so get rid of it
			packets[bestIngredient] = packets[bestIngredient][1:] # get rid of leading element
			continue
		foundNumber = False
		for numRecipies in range(smallestNumRecipies, largestNumRecipies + 1):
			canMake = True
			for ingredient in range(numIngredients):
				ratio = float(packets[ingredient][0]) / float(amountsNeeded[ingredient])
				if ratio / .9 < numRecipies or ratio / 1.1 > numRecipies:
					# can't make this number of recipies
					canMake = False
					break
			if canMake:
				numGroups += 1
				foundNumber = True
				for ingredient in range(numIngredients):
					packets[ingredient] = packets[ingredient][1:] # get rid of leading element
				break
		if not foundNumber:
			# couldn't make a recipie, so just trash the smallest (by ratio) packet
			packets[bestIngredient] = packets[bestIngredient][1:] # get rid of leading element
	print("Case #" + str(i + 1) + ": " + str(numGroups))