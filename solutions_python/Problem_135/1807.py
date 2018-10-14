file_input = open('MagicTrick_input')
file_output = open('MagicTrick_output', 'w')

T = int(file_input.readline())

for i in range(T):
	row1 = int(file_input.readline())
	cards1 = []
	for __ in range(4):
		line = list(map(int, file_input.readline().split()))
		cards1.append(line)
	row2 = int(file_input.readline())
	cards2 = []
	for __ in range(4):
		line = list(map(int, file_input.readline().split()))
		cards2.append(line)
	
	set1 = set(cards1[row1 - 1]) # Offsetting indices by 1
	list2 = cards2[row2 - 1] # Offsetting indices by 1
	intersection = [val for val in list2 if val in set1]

	if len(intersection) == 0:
		file_output.write('Case #' + str(i + 1) + ': Volunteer cheated!\n')
	elif len(intersection) == 1:
		file_output.write('Case #' + str(i + 1) + ': ' + str(intersection[0]) + '\n')
	else:
		file_output.write('Case #' + str(i + 1) + ': Bad magician!\n')



