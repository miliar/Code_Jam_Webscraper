input_file = open("ex.in")
output_file = open('ex.out', 'w')
def next_line():
	return input_file.readline()
cases = int(next_line())
for case_number in range(cases):
	done = False
	first_answer = int(next_line())-1
	rows1 = []
	for i in range(4):
		rows1.append(next_line().split( ))
	second_answer = int(next_line())-1
	rows2 = []
	for i in range(4):
		rows2.append(next_line().split( ))
	answer = 0
	for card in rows2[second_answer]:
		print str(rows1) + '-' + str(card)
		if card in rows1[first_answer]:
			if answer:
				output_file.write('Case #'+str(case_number+1)+': Bad magician!\n')
				done = True
				break
			answer = card
	if done: continue
	if not answer:
		output_file.write('Case #'+str(case_number+1)+': Volunteer cheated!\n')
	else:
		output_file.write('Case #'+str(case_number+1)+': '+answer+'\n')

