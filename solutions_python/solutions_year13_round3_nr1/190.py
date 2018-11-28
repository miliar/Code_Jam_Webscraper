#!/usr/bin/python3

# T-30 seconds...

#GO

# Grab each possible block of n consonants
# Rolling scan probably, indicate the length of each block
# Substrings will be... each block, + 1 for each remaining character in the length

# xyzz
# xyz + xyzz
# yzz + xyzz
# Need to do something about ordering to prevent overlap
# Is only calculating forwards sufficient?
# No, because axyza needs to yeld axyz, xyza, axyza, xyz

# Need to generate substrings on a per-block basis
# So generate all suitable substrings out of the consonant block and... err... how to factor in the rest of the string?
# Only blocks containing the first char need to generate backwards
# """ last """ forwards

# axyzza
# _xyz__
# __yzz_

# Hrmm, Find the length of the consonant block and handle multiple cases?
# left case and right case are symmetrical
# Then the everything case... that somehow doesn't overlap with the rest?
# Storing the generated list will work for the small set, maybe not large

# Can store a list of generated bounds instead - once generation reaches an existing bound, anything further will
# overlap
# axyzza - first bound will be [xyz]

# reductive/exploding case - n=1, string is 100 consonants
# Becomes generate everything possible substring

# Hrmmm, is tree-izing the string a scalable solution?
# Locate all the possible consonant blocks of length n, cut up the string so it fits...
# Or just do a scan of the string to check if a suitable block still exists on each side?
# Sounds slow and... explosive

# Substrings of length L: 1 if there's a suitable string in there somewhere
# 

# !!!!!! Remap the string to consonant/non-consonant

# So the problem becomes, how many substrings can be generated out of the string containing at least one consonant
# block?

# Maximum number of substrings is on the order of L^2?
# L+L-1+L-2...
# HRMMM... from the first character in the string, to the end of the first consonant block, * the number of characters
# remaining in the string
# From the second character... same thing

# Except it's not the first consonant block, it's first consant block that is entirely after the start point
# Can just scan forwards... 
vowels = "aeiou"

cases = int(input())
for case in range(1, cases+1):
	str, n = input().split()
	n = int(n)
	name = [1 if x in vowels else 0 for x in str]
	#print(name)
	#print(n)
	
	#starts = set()
	#consonants = 0
	nval = 0
#	for idx, char in enumerate(name):
#		if char:
#			consonants = 0
#			continue
#		consonants += 1
#		if consonants >= n:
#			starts.add(idx - n + 1)
	block = -1 # Start point of the next consonant block
	for start, char in enumerate(name):
		if block < start:
			consonants = 0
			for x in range(start, len(name)):
				if name[x]:
					consonants = 0
					continue
				consonants += 1
				if consonants >= n:
					block = x - n + 1
					#print("Found block ending at %s" % x)
					break
		if block < start: # Still less than start, no more blocks to find
			break
		if block >= start:
			#print("Adding %s to %s" % (start, block))
			nval += len(name) - (block + n) + 1
			#print("%s" % str[start:block+n])

	print("Case #%s: %s" % (case, nval))
