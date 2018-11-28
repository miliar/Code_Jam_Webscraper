# print "hello world!"

FILE = "A-large.in"

number_of_inputs = 0
inp = []

with open(FILE, "r") as f:
	number_of_inputs = int(f.readline())
	for line in f:
		inp.append(line.split("\n")[0])


assert number_of_inputs == len(inp)

for pos, entry in enumerate(inp):
	pos += 1

	num_of_groups = int(entry.split(" ")[0]) + 1
	people_per_group = entry.split(" ")[1]

	# Test full group edge case
	full_group = True
	for group in people_per_group:
		if int(group) == 0:
			full_group = False

	# Other cases
	total_people_needed = 0
	total_people_at_a_point = int(people_per_group[0])
	# print total_people_at_a_point

	for group, total_in_group in enumerate(people_per_group[1:]):
		group += 1
		if total_people_at_a_point < group:
			total_people_needed += 1
			total_people_at_a_point += 1
		total_people_at_a_point += int(total_in_group)

	# print total_people_needed


	if full_group:
		print "Case #{}: 0".format(pos)
	else:
		print "Case #{}: {}".format(pos, total_people_needed)