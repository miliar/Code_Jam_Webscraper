def problemA(input_file, output_file):
	with open(input_file, 'rb')as f:
		T = int(f.readline())
		case = 1
		for line in f:
			if len(line) > 0:
				num_friends_needed = 0
				people_standing = 0
				S_max, S = line.rstrip().split(" ")
				for i in xrange(int(S_max) + 1):
					num_shy_i_people = int(S[i]) # number of people with shy i
					if num_shy_i_people > 0: # if there are people with shy i
						if people_standing >= i: # if i people standing, then all shy i people stand
							people_standing += num_shy_i_people
						else: # otherwise, need to bring in some friends to make them stand
							# Greedily bring in people with shy = people_standing
							num_bring_in = i - people_standing
							num_friends_needed += num_bring_in
							people_standing += num_bring_in + num_shy_i_people
				with open(output_file, 'ab') as o:
					o.write("Case #" + str(case) + ": " + str(num_friends_needed) + "\n")
				case += 1


if __name__ == "__main__":
	input_file = "A-large.in"
	# input_file = "sample_input.txt"
	output_file = "output_large.txt"
	problemA(input_file, output_file)
