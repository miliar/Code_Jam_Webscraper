msg_bad_magician = 'Bad magician!'
msg_volunteer_cheated = 'Volunteer cheated!'

with open('input.txt') as f:
	content = f.readlines()

out = open('output.txt', 'w')

cases = int(content[0])

for case in range(cases):
	case_offset = case * 10
	
	answer1 = int(content[1 + case_offset])
	cards1 = content[2 + case_offset:6 + case_offset]
	
	answer2 = int(content[6 + case_offset])
	cards2 = content[7 + case_offset:11 + case_offset]
	
	answer1_row = cards1[answer1 - 1].replace('\n', '').split(' ')
	answer2_row = cards2[answer2 - 1].replace('\n', '').split(' ')

	num_in_same_row = 0
	num_volunteer_picked = 0

	for num in answer1_row:
		if num in answer2_row:
			num_in_same_row += 1
			num_volunteer_picked = num

	if num_in_same_row == 0:
		out.write('Case #{0}: {1}\n'.format(case + 1, msg_volunteer_cheated))
	elif num_in_same_row > 1:
		out.write('Case #{0}: {1}\n'.format(case + 1, msg_bad_magician))
	else:
		out.write('Case #{0}: {1}\n'.format(case + 1, num_volunteer_picked))

out.close()