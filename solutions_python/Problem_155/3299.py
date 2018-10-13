#!/usr/bin/python
# this script is compatible with python 3.4

for N in range(int(input())):
	max_shyness, audience  = input().split()
	audience = [int(c) for c in audience]
	added = 0
	total = 0
	for i in range(len(audience)):  # i is shyness level
		if total < i:  # if people with shyness level i won't stand up
			# add friends to get these people to stand up
			friends = i - total
			total += friends  # total is i
			added += friends
		# the people of shyness level i stand up
		total += audience[i]  # total audience members updated
	print("Case #{}: {}".format(N+1, added), end="\n")
