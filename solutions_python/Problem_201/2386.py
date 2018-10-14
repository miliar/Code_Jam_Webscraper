#NOBODY WILL EVER LEAVE!!!!!!11!!

def generate_output(case, max_val, min_val):
	return "Case #" + str(case) + ": " + str(max_val) + " " + str(min_val)

def imprison_in_stall_forever(spot_width):
	if spot_width == 1:
		return 0, 0
	elif spot_width % 2 != 0:
		result = (spot_width - 1)/2
		return result, result
	else:
		result = (spot_width)/2
		return result, result - 1

def solve_case(nb_stalls, nb_prisoners):
	empty_slots = [nb_stalls]
	for i in range(0, nb_prisoners):
		empty_slots = sorted(empty_slots)
		max_value, min_value = imprison_in_stall_forever(empty_slots.pop())
		empty_slots.append(max_value)
		empty_slots.append(min_value)

	return max_value, min_value



with open("C-small-1-attempt0.in", "r") as dataset:
	nb_cases = dataset.readline().rstrip("\n")
	output_result = []
	case_nb = 1
	for line in dataset:
		input_case = line.rstrip('\n').split(' ')
		nb_stalls = int(input_case[0])
		nb_prisoners = int(input_case[1])
		max_val, min_val =  solve_case(nb_stalls, nb_prisoners)
		output_result.append(generate_output(case_nb, max_val, min_val))
		case_nb += 1

	with open("result.txt", "w+") as output_file:
		for line in output_result:
			output_file.write(line + "\n")