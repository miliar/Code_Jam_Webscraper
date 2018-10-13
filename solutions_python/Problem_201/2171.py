import math
import itertools
from collections import defaultdict


def main():

	NumberOfTestCases = int(input())

	for T in range(1, NumberOfTestCases+1):

		N, K = map(int, input().split())

		maxLsRs, minLsRs = stalls(N ,K)

		print( "Case #" + str(T) + ": " + str(maxLsRs) + " " + str(minLsRs) )


def even(n): return n % 2 == 0
def odd(n): return n % 2 == 1


def stalls(num_stalls, num_people):


	# print("num people " +str(num_people))

	# if num_people > num_stalls / 2.0: return (0, 0)

	nearest_power_of_2_below = math.floor(math.log(num_people,2))

	# print("nearest_power_of_2_below " + str(nearest_power_of_2_below))
	# print("I'm going to use " + str(2**nearest_power_of_2_below - 1) + " people ")

	num_people = num_people - (2**nearest_power_of_2_below - 1)

	# print("I have "+str(num_people)+" people left")

	sections = [(num_stalls, 1)]
	new_sections = []

	for halving in range(nearest_power_of_2_below):

		for section_size, count in sections:

			if odd(section_size):

				new_sections.append(((section_size - 1) / 2, count * 2))

			else:
				assert even(section_size)

				new_sections.append(((section_size - 2) / 2, count))
				new_sections.append(((section_size) / 2, count))

		sections = new_sections
		new_sections = []

	dd = defaultdict(int)
	for section_size, count in sections:
		dd[section_size] += count

	sections = list(reversed(sorted(dd.items())))

	# print("I now have size x sections of quantity y")
	# print(sections)

	# At this point, there are two section sizes left.
	# We want to fill up the bigger one first.

	# If we can fill up the bigger one, then the last person will find a stall in the smaller one
	if sections[0][1] < num_people:

		section_size = sections[1][0]

	# if we can't fill up the bigger one, then the last person will find a stall in the larger one
	elif sections[0][1] >= num_people:

		section_size = sections[0][0]


	if section_size == 1: return (0, 0)
	elif odd(section_size): return (int((section_size - 1) / 2), int((section_size - 1) / 2))
	else: return (int(section_size / 2), int((section_size - 2) / 2))






# def stalls(num_stalls, num_people):

# 	sections = [num_stalls]
# 	flag = False

# 	for person in range(num_people - 1):

# 		max_size = max(sections)
# 		# print("person #" + str(person+1) + " finds max size " + str(max_size))

# 		section_index = sections.index(max_size)

# 		if max_size == 1:

# 			del sections[section_index]

# 			flag = True
# 			minLsRs = 0

# 		elif odd(max_size):

# 			del sections[section_index]
# 			sections.insert(section_index, int((max_size - 1) / 2))
# 			sections.insert(section_index, int((max_size - 1) / 2))

# 		else: # even(max_size)

# 			del sections[section_index]
# 			sections.insert(section_index, int((max_size) / 2))
# 			sections.insert(section_index, int((max_size - 2) / 2))

# 		sections = list(filter((0).__ne__, sections))

# 		print(sections)

# 	section_size = max(sections)

# 	if section_size == 1: return (0, 0)
# 	elif odd(section_size): return (int((section_size - 1) / 2), int((section_size - 1) / 2))
# 	else: return (int(section_size / 2), int((section_size - 2) / 2))





main()









