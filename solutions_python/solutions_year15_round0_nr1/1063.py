input_file = open("A-large.in")
output_file = open("out", "w")

T = int(input_file.readline().strip())
for t in range(T):
	s_levels = list(map(int, input_file.readline().strip().split(" ")[1]))
	# print(s_levels)

	people_needed = 0
	people_standing = 0
	for i, x in enumerate(s_levels):
		# print(i, x, people_standing, people_needed)

		if people_standing >= i:
			people_standing += x
		else:
			people_needed += i - people_standing
			people_standing = i + x

	# print(people_standing, people_needed)
	# print("Case #{0}: {1}".format(t + 1, people_needed))
	# print()
	output_file.write("Case #{0}: {1}\n".format(t + 1, people_needed))
