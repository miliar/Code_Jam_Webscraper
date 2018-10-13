def parse_input(file_name):

	input = []
	cases = 0

	with open(file_name) as data:
		for line in data:
			if len(line.split()) == 1:
				cases = line.split()
			elif len(line.split()) == 2:
				input.append(line.split())

	return cases, input


def flip(pancake):

	flipped_pancake = ''	
	if pancake == '-':
		flipped_pancake = '+'
	elif pancake == '+':
		flipped_pancake = '-'

	return flipped_pancake

def save_to_file(data, file_name):
	file = open(file_name, 'w')
	for item in data:
  		file.write("%s\n" % item)
	file.close()


def pancakes():

	cases_nb, cases = parse_input('input')
	# print cases_nb, cases

	output = []
	flips = 0
	possible = True
	for id, case in enumerate(cases):
	
		if len(case[0]) < int(case[1]):
			output.append('Case #' + str(id + 1) + ': IMPOSSIBLE')
			break

		# do the flippin
		pancakes = list(case[0])
		new_id = 0
		for _id, pancake in enumerate(pancakes):
			# print pancakes
			if pancake == '-' and _id + int(case[1]) <= len(pancakes):
				flips += 1
				for i in range(_id, _id + int(case[1])):
					pancakes[i] = flip(pancakes[i])
					if pancakes[i] == '-' and save == True:
						new_id = i
						save = False
				_id = new_id
				save = True

			elif pancake == '-':
				possible = False
				break

		if possible:
			output.append('Case #' + str(id + 1) + ': ' + str(flips))
		else:
			output.append('Case #' + str(id + 1) + ': IMPOSSIBLE')
		flips = 0
		possible = True

	save_to_file(output, 'output')


pancakes()