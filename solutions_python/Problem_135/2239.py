import fileinput

input_string = ""
for line in fileinput.input():
	input_string += line

input_array = input_string.rstrip().split("\n")
test_cases = int(input_array[0])

for x in xrange(0, test_cases):
	row = int(input_array[x*10+1])
	first_potential_cards = map(int, input_array[1+x*10+row].rstrip().split(" "))
	# print first_potential_cards
	second_row = int(input_array[x*10+6])
	second_potential_cards = map(int, input_array[6+x*10+second_row].rstrip().split(" "))
	# print second_potential_cards

	matches = []
	for i in first_potential_cards:
		if i in second_potential_cards:
			matches.append(i)

	print "Case #" + str(x+1) + ": ",

	if len(matches) == 0:
		print "Volunteer cheated!"
	elif len(matches) > 1:
		print "Bad magician!"
	else:
		print matches[0]