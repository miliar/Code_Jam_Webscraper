import fileinput
import sys

# 4
# 3 1 5 15 13 11
# 3 0 8 23 22 21
# 2 1 1 8 0
# 6 2 8 29 20 8 18 18 21
# | | | `--`--`-`--`--`--sums for players
# | | `- p - best result of at least this is what we're finding
# | `- S - number of surprising triples
# `- N - number of googles

def doit(numSurprises, p, list_of_sums):
	if p == 0:
		# special case
		return len(list_of_sums)

	which_section = 0 #0 means can't be done, 1 means need a surprise, 2 means guarantee
	count1 = 0
	count2 = 0

	list_of_sums = [int(i) for i in list_of_sums]
	list_of_sums.sort()

	for su in list_of_sums:
		if which_section == 0:
			if p == 1: # if p is 1 then we never need surprises
				if su > 0:
					which_section = 2
				else:
					continue
			elif su >= 2 + 3*(p-2):
				#print("leaving 0 at " + str(su) + " which is greater than " + str(2 + 3*(p-2)))
				which_section = 1
			else:
				continue

		if which_section == 1:
			if su >= 1 + 3*(p-1):
				#print("leaving 1 at " + str(su) + " which is greater than " + str(1 + 3*(p-1)))
				which_section = 2
			else:
				count1 += 1
				continue

		if which_section == 2:
			count2 += 1

	return count2 + min(count1, numSurprises)




i = 1
firstone = True
for line in fileinput.input():
	if firstone:
		firstone = False
		continue
	sys.stdout.write("Case #" + str(i) + ": ")

	# parse it; parse it good

	splitline = line.split(' ')

	sys.stdout.write(str(doit(int(splitline[1]), int(splitline[2]), splitline[3:])))


	sys.stdout.write('\n')
	i+=1
