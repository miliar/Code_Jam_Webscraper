def repeater(strings):
	string_letters = []
	letter_count = []
	for string in strings:
		letters = string[0]
		letter_count.append([0])
		for letter in string:
			if letter != letters[-1][-1]:
				letters += letter
				letter_count[-1].append(1)
			else:
				letter_count[-1][-1] += 1
		string_letters.append(letters)
		if letters != string_letters[0]: return "Fegla Won"
	
	moves = 0
	for letter_counts in zip(*letter_count):
		letter_counts = sorted(letter_counts)
		high_index = len(letter_counts) - 1
		low_index = 0
		num_high_counts = 1
		num_low_counts = 1
		while high_index > low_index:
			moves += (letter_counts[high_index] - letter_counts[high_index - 1]) * num_high_counts
			num_high_counts += 1
			high_index -= 1
			if high_index > low_index:
				moves += (letter_counts[low_index] - letter_counts[low_index + 1]) * num_low_counts
				num_low_counts += 1
		
	return str(moves)


for T in range(int(raw_input())):
	strings = []
	for i in range(int(raw_input())):
		strings.append(raw_input())
	print "Case #%d: %s" % (T+1, repeater(strings))