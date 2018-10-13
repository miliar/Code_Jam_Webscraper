#!/usr/bin/env python3

num_cases = int(input())

for i in range(0,num_cases):
	to_add = 0
	line = input().split()
	max_shy = int(line[0])
	audience = line[1]

	people_standing = int(audience[0])
	# We don't care about people with shyness 0,
	# They'll stand up anyway. Sheep.
	for a in range(1,max_shy + 1):
		cur_shy = int(audience[a])

		#print("{} people standing. Need {} people.".format(people_standing, a))
		while (people_standing < a):
			#print("Adding a friend!")
			people_standing += 1
			to_add += 1
		people_standing += cur_shy

	print("Case #{}: {}".format(i + 1, to_add))
