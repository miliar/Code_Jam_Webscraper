REPEAT = 17
CHEAT  = 18
PRINT_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, "Bad magician!", "Volunteer cheated!"]

input = "input.txt"
with open(input, 'r') as infile:
	cases = int(infile.readline())
	results = [0] * cases
	
	for case in range(cases):
		row_start = int(infile.readline())
		# print("row_start: ", row_start)
		mat_start = []
		mat_start.append(infile.readline().split())
		mat_start.append(infile.readline().split())
		mat_start.append(infile.readline().split())
		mat_start.append(infile.readline().split())
		init_row = mat_start[row_start - 1]
		# print("init row: ", init_row)

		
		row_end = int(infile.readline())
		# print("row_end: ", row_end)
		mat_end = []
		mat_end.append(infile.readline().split())
		mat_end.append(infile.readline().split())
		mat_end.append(infile.readline().split())
		mat_end.append(infile.readline().split())
		final_row = mat_end[row_end - 1]
		# print("final row: ", final_row)
		
		# now have initial and final rows, compare for common #
		for init in init_row:
			for final in final_row:
				# print("init: ", init, "final: ", final)
				if init == final:  # found match
					# print("matched")
					results[case] = int(init) if results[case] == 0 else REPEAT
	
	# print out case results
	for case in range(cases):
		print("Case #{}: {}".format(case + 1, PRINT_ARRAY[results[case] - 1]))
		