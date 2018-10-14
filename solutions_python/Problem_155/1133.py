
def read(path):
	file_in = open(path, 'r')

	# No file out; Use "python A.py > A_out_small.txt"

	case = 0
	start = 0
	for line in file_in:
		if case == 0:
			case += 1
		else:
			data = line.split()
			# Use the first and second to the people
			needed = people(int(data[0]), data[1])

			print "Case #" + str(case) + ": " + str(needed)
			case += 1


def people(max_shy, strin):
	up = 0
	needed = 0
	for i in range(len(strin)):
		# Get each number of people
		if i == 0:
			up += int(strin[i])
		else:
			if up < i:
				needed += i - up
				up += i - up
				up += int(strin[i])
			else:
				up += int(strin[i])
	return needed

# read("A_tests.txt")
# read("A-small-attempt1.in")
read("A-large.in")