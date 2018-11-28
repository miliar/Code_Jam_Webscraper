input_file = open("A-small-attempt3.in", encoding="utf-8")
input_data = input_file.read().split("\n")

input_data.pop(0)
input_data.pop()
i = 1

while input_data:
	count = 0
	first_row, first_card, second_row, second_card = input_data[0], input_data[1:5], input_data[5], input_data[6:10]
	input_data[:10] = []
	first_element = first_card[int(first_row)-1].split(" ")
	second_element = second_card[int(second_row)-1].split(" ")
	for element in first_element:
		if element in second_element:
			answer = element
			count += 1
	if count == 1:
		print("Case #{:d}: {:s}".format(i,answer))
	elif count >= 2:
		print("Case #{:d}: Bad magician!".format(i))
	elif count == 0:
		print("Case #{:d}: Volunteer cheated!".format(i))
	i += 1

input_file.close()