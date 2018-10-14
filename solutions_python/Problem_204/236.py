import math

file_strings = []
with open("Rat.txt") as data_file:
	for line in data_file:
		file_strings.append(line.strip())

T = file_strings[0] # number of testcases
file_strings.pop(0)
T = int(T)

for i in range(1, T + 1):
	vals = file_strings.pop(0).split()
	N, P = int(vals[0]), int(vals[1]	)
	# N is number of ingredients, P is number of packages - rows and columns
	serving_quants = [int(x) for x in file_strings.pop(0).split()]
	# packages is packages[ingredient][package number]
	packages = []
	# index of how far to the right we are in each row
	indices = []
	for j in range(N):
		packages.append([int(x) for x in file_strings.pop(0).split()])
		packages[j].sort()
		indices.append(0)

	count = 0 # we output count
	toolarge = False
	k = 1 # the number of servings we're looking to make in our kit
	while(not toolarge):
		lowerbound = [(0.9 * x * k) for x in serving_quants]
		upperbound = [(1.1 * x * k) for x in serving_quants]
		possible = True
		for ingred in range(len(packages)):
			if(indices[ingred] == P):
				toolarge = True
				break
			while(packages[ingred][indices[ingred]] < lowerbound[ingred]):
				indices[ingred] = indices[ingred] + 1
				if(indices[ingred] == P):
					toolarge = True
					break
			if toolarge:
				break
			if packages[ingred][indices[ingred]] > upperbound[ingred]:
				possible = False
				break

		if (not possible):
			k = k +1
		elif (not((not possible) or toolarge)):
			count = count + 1
			for ingred in range(N):
				indices[ingred] = indices[ingred] + 1

	print("Case #{}: {}".format(i, count))


			
