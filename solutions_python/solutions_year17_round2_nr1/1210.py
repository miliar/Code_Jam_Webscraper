def parse_input(file_name):

	input = []
	cases = 0
	case = []
	cnt = 0
	caseCnt = 0
	with open(file_name) as data:
		for id, line in enumerate(data):
			if id == 0:
				cases = line.split()
				caseCnt = int(cases[0])

			elif cnt == 0:
				input.append(case)
				case = []
				case.append(line.split())
				cnt = int(line.split()[1])
				caseCnt -= 1

			else:
				case.append(line.split())
				cnt -= 1

			if caseCnt == 0 and cnt == 0:
				input.append(case)

	input.pop(0)
	return cases, input

def save_to_file(data, file_name):
	file = open(file_name, 'w')
	for item in data:
  		file.write("%s\n" % item)
	file.close()

def horse():

	cases_nb, cases = parse_input('input')

	output = []
	slowest_horse = -1
	for id, case in enumerate(cases):
		print case
		for _id, horse in enumerate(case):

			if _id == 0:
				annie_dist = int(horse[0])
			else:
				horse_dist = int(horse[0])
				horse_speed = int(horse[1])
				current_horse = (annie_dist - horse_dist)*1.0 / horse_speed
				if current_horse > slowest_horse:
					slowest_horse = current_horse

		annie_speed = annie_dist*1.0 / slowest_horse
		slowest_horse = -1
		output.append('Case #' + str(id + 1) + ': ' + str(annie_speed))

	return output


save_to_file(horse(), 'output') 