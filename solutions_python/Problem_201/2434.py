
def main(num_stalls, num_people):
	og_stalls = num_stalls
	sections = []
	sections.append(num_stalls)
	for peeps in range(num_people):
		num_stalls = max(sections)
		del sections[sections.index(num_stalls)]
		if num_stalls%2 != 0:
			# That person goes center
			Ls = (num_stalls-1)/2
			Rs = (num_stalls-1)/2
			sections.append(Ls)
			sections.append(Rs)
		else:
			Ls = (num_stalls/2)-1
			Rs = (num_stalls/2)
			sections.append(Ls)
			sections.append(Rs)
		# if Ls > Rs:
		# 	num_stalls = Ls
		# else:
		# 	num_stalls = Rs
	# if og_stalls == num_people:
	# 	Ls = 0
	# 	Rs = 0
	# if Ls < 0:
	# 	Ls = 0
	# if Rs < 0:
	# 	Rs = 0
	return int(Ls), int(Rs)

if __name__ == "__main__":
	with open('C-small-1-attempt1.in', 'r') as f:
		lines = f.readlines()

	case = 1
	string_answers = []
	for l in lines[1:len(lines)]:
		l = l.strip().split()
		num_stalls = int(l[0])
		num_people = int(l[1])
		Ls, Rs = main(num_stalls, num_people)
		string = "Case #" + str(case) + ": " + str(Rs) + ' ' + str(Ls) + '\n'
		string_answers.append(string)
		print(string)
		case = case + 1

	with open('result1.txt', 'w') as k:
		for ans in string_answers:
			k.write(ans)