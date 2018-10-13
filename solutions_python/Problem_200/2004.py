
def save_to_file(data, file_name):
	file = open(file_name, 'w')
	for item in data:
  		file.write("%s\n" % item)
	file.close()


def parse_input(file_name):

	input = []
	cases = 0

	with open(file_name) as data:
		for line in data:
			if len(line.split()) == 1:
				input.append(line.split())

	cases = input.pop(0)
	return cases, input

def tidy():

	cases, input_data = parse_input('input')

	output = []
	for idd, nb in enumerate(input_data):
		list_nb = map(int, list(nb[0]))
		_id = -1
		_id_zero = -1
		
		for i in range(len(list_nb)-1):

			if list_nb[i] > list_nb[i+1]:	
				_id = i
				list_nb[i] -= 1	
				for k in range(_id, 0, -1):
					if list_nb[k] < list_nb[k-1]:
						list_nb[k-1] = list_nb[k]
						_id = k-1
						if list_nb[k] == 0:
							list_nb[k] = 9
					else:
						break
				break

		if _id != -1:
			nines = len(list_nb) - (_id + 1)
			list_nb = list_nb[:_id + 1]
			for _ in range( nines ):
				list_nb.append(9)
			if list_nb[0] == 0:
				list_nb.pop(0)


		output.append('Case #' + str(idd + 1) + ': ' + ''.join(map(str, list_nb)))

	return output
	# for nb in input_data:
	# 	list_nb = map(int, list(nb[0]))

	# 	_id = -1
	# 	result = []
	# 	for i in range(len(list_nb) - 1, 0, -1):
	# 		if list_nb[i] < list_nb[i-1]:	
	# 			_id = i
	# 			list_nb[i-1] -= 1	
			
	# 	if _id == -1:
	# 		print list_nb
	# 		continue	
	# 	else:
	# 		result = list_nb[:_id]
	# 		for _ in range(len(list_nb) - _id):
	# 			result.append(9)
	# 	print result

def main():

	output =  tidy()
	# print output
	save_to_file(output, 'output')

main()