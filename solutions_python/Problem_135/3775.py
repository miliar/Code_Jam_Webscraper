in_file = open("A-small-attempt1.in")
cards = in_file.readlines()
in_file.close()
result_arr = []
cards = cards[1:]

for row in range(int(len(cards)/10)):
	ind = row * 10
	first_row_ind = int(cards[ind]) + ind
	first_row = cards[first_row_ind].split()
	second_row_ind = int(cards[ind + 5])+5 + ind
	second_row = cards[second_row_ind].split()
	result = (set(first_row) & set(second_row))

	if len(result) == 1:
		result_arr.append("Case #" + str(row+1) + ": " + list(result)[0] + "\n")
	elif len(result) > 1:
		result_arr.append("Case #" + str(row+1) + ": " + "Bad magician!" + "\n")
	else:
		result_arr.append("Case #" + str(row+1) + ": " + "Volunteer cheated!" + "\n")

file_out = open("A-small-attempt1.out", "w+")
file_out.writelines(result_arr)
file_out.close()