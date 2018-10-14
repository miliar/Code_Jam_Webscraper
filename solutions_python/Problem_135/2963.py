import operator

def solve(row_input1, row_input2):
	intersec = list(set(row_input1).intersection(row_input2))
	count = len(intersec)

	if count == 0:
		return "Volunteer cheated!"
	elif count == 1:
		return intersec[0]
	else:
		return "Bad magician!"	

def string_to_vect(value):
	return map(int, value.split(" "))

def get_selected_row():
	selected_row = int(raw_input())
	
	row_counter = 1
		
	while (row_counter <= 4):
		row_raw_input = raw_input()
			
		if row_counter == selected_row:
			row_input = row_raw_input
			
		row_counter += 1
		
	return string_to_vect(row_input)

if __name__ == "__main__":
	test_cases = input()
     
	for case in xrange(1, test_cases + 1):
		row_input1 = get_selected_row()
		row_input2 = get_selected_row()
		
		print "Case #%i: %s" % (case, solve(row_input1, row_input2))
