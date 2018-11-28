#!/usr/bin/python

import re

r = open('input.txt', 'r')
inputs = []
for line in r:
	inputs.append(line.strip())

num_cases = int(inputs.pop(0))
i = 1
instance = []
while (i <= num_cases):
	instance = re.split(' ', inputs[i-1])
	j = 0
	# Go through each index (j).
	num_clapping = 0
	needed = 0
	people = instance[1]
	#print people
	while (j <= int(instance[0])):
		#print "Index " + str(j) + ": " + str(num_clapping + needed) + " people clapping and " + str(j) + " needed for all people to clap."
		if j > (num_clapping + needed):
			needed += (j - num_clapping - needed)
			#print "Not enough people"
		num_clapping += int(people[j])
		j += 1
	print "Case #" + str(i) + ": " + str(needed)
	i += 1;