
import math 

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

def save_to_file(data, file_name):
	file = open('output', 'w')
	for item in data:
  		file.write("%s\n" % item)
	file.close()

def bathroom(N, K):

	occupied = [[0, N+1]]
	left = [0] * K
	right = [0] * K
	

	for k in range(K):

		if k > N-1:
			break
		
		best_range = occupied.pop(0)
		best = (best_range[1] - best_range[0]) / 2
		best += best_range[0]
		
		left[k] = best - best_range[0] - 1
		right[k] = best_range[1] - best  - 1

		tmp_list = []
		if left[k] > 0: 
			tmp_list.append([best_range[0], best])

		if right[k] > 0:

			if tmp_list != [] and (tmp_list[0][1] - tmp_list[0][0] < best_range[1] - best): 		
				tmp = tmp_list.pop()
				tmp_list.append([best, best_range[1]])
				tmp_list.append(tmp)
			else:
				tmp_list.append([best, best_range[1]])

		if k == 0:
			if len(tmp_list) > 0:
				occupied.append(tmp_list[0])
			if len(tmp_list) > 1:
				occupied.append(tmp_list[1])
		else:
		
			for id, _range in enumerate(occupied):
				if tmp_list != []:
					if _range[1] - _range[0] < tmp_list[0][1] - tmp_list[0][0] or (_range[1] - _range[0] == tmp_list[0][1] - tmp_list[0][0] and _range[0] > tmp_list[0][0] ):
						occupied.insert(id, tmp_list[0])
						tmp_list.pop(0)
		
			for item in tmp_list:
				occupied.append(item)
			tmp_list = []
		# occupied.append(tmp)

	# for k in range(K):
	# 	if k > N-1:
	# 		break
	# 	best = (occupied[k][1] - occupied[k][0]) / 2
	# 	best = occupied[k][0] + best
		
	# 	left[k] = best - occupied[k][0] - 1
	# 	right[k] = occupied[k][1] - best  - 1

	# 	last = occupied[-1][1] - occupied[-1][0]
	# 	tmp_list = []

	# 	if left[k] > 0: 
	# 		tmp_list.append([occupied[k][0], best])

	# 	if right[k] > 0:

	# 		if tmp_list != [] and (tmp_list[0][1] - tmp_list[0][0] < occupied[k][1] - best): 		
	# 			tmp = tmp_list.pop()
	# 			tmp_list.append([best, occupied[k][1]])
	# 			tmp_list.append(tmp)
	# 		else:
	# 			tmp_list.append([best, occupied[k][1]])

	# 	for tmp in tmp_list:
	# 		if k != 0:
	# 			last_item = occupied.pop()
	# 			second_to_last = occupied.pop()
	# 			asd_list = []
	# 			if tmp[1] - tmp[0] < second_to_last[1] - second_to_last[0] or (second_to_last[0] < tmp[0]) and (tmp[1] - tmp[0] == second_to_last[1] - second_to_last[0]):
	# 				asd_list.append(second_to_last)
	# 			if tmp[1] - tmp[0] < last_item[1] - last_item[0] or (last_item[0] < tmp[0]) and (tmp[1] - tmp[0] == last_item[1] - last_item[0]):
	# 				asd_list.append(last_item)

	# 			asd_list.append(tmp)
	# 			if len(asd_list) == 1:
	# 				asd_list.append(second_to_last)
	# 				asd_list.append(last_item)
	# 			elif len(asd_list) == 2:
	# 				asd_list.append(last_item)

	# 			for asd in asd_list:
	# 				occupied.append(asd)
	# 		else:
	# 			occupied.append(tmp)


		# print k+1, best, occupied, left[k], right[k]
		# last = occupied[-1][1] - occupied[-1][0]
		# if (occupied[k][1] - occupied[k][0]) % 2 != 0:
		# 	if right[k] > 0:
		# 		if occupied[k][1] - best > last or (occupied[k][1] - best == last and best < occupied[-1][0]):
		# 			tmp = occupied.pop()
		# 			occupied.append([best, occupied[k][1]])
		# 			occupied.append(tmp)
		# 		else:
		# 			occupied.append([best, occupied[k][1]])
		# 	if left[k] > 0:
		# 		if best - occupied[k][0] > last or (best - occupied[k][0] == last and best < occupied[-1][0]):
		# 				tmp = occupied.pop()
		# 				occupied.append([occupied[k][0], best])
		# 				occupied.append(tmp)
		# 		else:
		# 			occupied.append([occupied[k][0], best])
		# else:
		# 	if left[k] > 0: 
		# 		if best - occupied[k][0] > last or (best - occupied[k][0] == last and best < occupied[-1][0]):
		# 				tmp = occupied.pop()
		# 				occupied.append([occupied[k][0], best])
		# 				occupied.append(tmp)
		# 		else:
		# 			occupied.append([occupied[k][0], best])

		# 	if right[k] > 0:
		# 		if occupied[k][1] - best > last or (occupied[k][1] - best == last and best < occupied[-1][0]):
		# 			tmp = occupied.pop()
		# 			occupied.append([best, occupied[k][1]])
		# 			occupied.append(tmp)
		# 		else:
		# 			occupied.append([best, occupied[k][1]])
		# print k+1, best, occupied, left[k], right[k]

	return max(left[K-1], right[K-1]), min(left[K-1], right[K-1])

def main():

	cases_nb, cases = parse_input('input')

	output = []
	for id, case in enumerate(cases):
		_max, _min = bathroom(int(case[0]), int(case[1]))
		output.append('Case #' + str(id + 1) + ': ' + str(_max) + ' ' + str(_min))

	save_to_file(output, 'output')
main()

