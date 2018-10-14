# last number is important because they have the highest threshold

def minimum_amount(audience):
	members_needed = 0
	audience_sum = 0
	for i in range(len(audience)):
		audience_amount = int(audience[i])
		if i > audience_sum and audience_amount > 0:
			new_members_needed = (i - audience_sum)
			members_needed += new_members_needed
			audience_sum += audience_amount + new_members_needed
		else:
			audience_sum += audience_amount

	return members_needed

def print_output(x, y):
	return "Case #" + str(x) + ": " + str(y) + "\n"

f =  open("A-small-attempt0.in", 'r')
test_cases = f.read().split("\n")[1:]
with open("output.txt", "w") as f:
	case_number = 1
	for test_case in test_cases:
		result = minimum_amount(test_case[2:])
		f.write(print_output(case_number, result))
		case_number += 1