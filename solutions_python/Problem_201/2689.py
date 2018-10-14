"""
Google Code Jam 2017
Question 3
"""

def empty_left(index, toilet_list):
	counter = 0
	current = index - 1
	while toilet_list[current] != 1:
		counter += 1
		current -= 1
	return counter

def empty_right(index, toilet_list):
	counter = 0
	current = index + 1
	while toilet_list[current] != 1:
		counter += 1
		current += 1
	return counter

def toilet(toilets, people):
	toilets_list = [0 for i in range(toilets + 2)]
	toilets_list[0] = 1
	toilets_list[-1] = 1
	for person in range(people):
		last_choice_max = 0
		last_choice_min = 0
		stall_dict = {}
		for index in range(1, len(toilets_list) - 1):
			if toilets_list[index] == 0:
				stall_dict[index] = [empty_left(index, toilets_list), empty_right(index, toilets_list)]
		val_dict = {}
		for key, val in stall_dict.items():
			val_dict[key] = min(val)
		maximum = max(val_dict.values())
		max_set = []
		for key, score in val_dict.items():
			if score == maximum:
				max_set.append(key)
		if len(max_set) == 1:
			toilets_list[max_set[0]] = 1
			last_choice_max = max(stall_dict[max_set[0]])
			last_choice_min = min(stall_dict[max_set[0]])
		else:
			val_dict2 = {}
			for key2 in max_set:
				val_dict2[key2] = max(stall_dict[key2])
			maximum2 = max(val_dict2.values())
			max_set2 = []
			for key3, score3 in val_dict2.items():
				if score3 == maximum2:
					max_set2.append(key3)
			if len(max_set2) == 1:
				toilets_list[max_set2[0]] = 1
				last_choice_max = max(stall_dict[max_set2[0]])
				last_choice_min = min(stall_dict[max_set2[0]])
			else:
				choice = min(max_set2)
				toilets_list[choice] = 1
				last_choice_max = max(stall_dict[choice])
				last_choice_min = min(stall_dict[choice])

	return last_choice_max, last_choice_min


t = int(raw_input().strip())
for i in range(t):
	q = raw_input().strip().split(' ')
	num_toilets = int(q[0])
	num_people = int(q[1])
	answer = toilet(num_toilets, num_people)
	print "Case #" + str(i + 1) + ": " + str(answer[0]) + " " + str(answer[1])


