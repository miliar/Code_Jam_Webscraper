import sys


# Read data file into a list
lines = []
with open(sys.argv[1], "r", encoding="utf-8") as data_file:
	for line in data_file:
		lines.append(line.rstrip('\n'))


# Get total number of test cases
test_cases = int(lines[0])
del lines[0]

# Process each test case
case = 0
for line in lines:
	
	case += 1
	input = [x for x in line.split(" ")]
	
	max_shyness = int(input[0])
	audience = str(input[1])
	
	total_standing = 0
	more_needed = 0
	
	for slot in range(max_shyness + 1):
		num_in_slot = int(audience[slot])
		if total_standing < slot:
			difference = slot - total_standing
			total_standing += num_in_slot + difference
			more_needed += difference
		else:
			total_standing += num_in_slot		

	print("Case #" + str(case) + ": " + str(more_needed))