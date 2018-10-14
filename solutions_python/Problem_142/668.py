import sys

input = open(sys.argv[1], 'r')

t = int(input.readline())

for case in range(1, t + 1):

	n = int(input.readline())
	
	strings = []
	for i in range(n):
		line = input.readline()
		if (line[-1] == '\n'):
			line = line[:-1]
		strings.append(line)
	
	string_run_lists = []
	for i in range(n):
		runs = []
		run_char = strings[i][0]
		run_length = 1
		
		for j in range(len(strings[i])):
			if (j + 1 >= len(strings[i])):
				runs.append((run_char, run_length))
			elif (strings[i][j + 1] != run_char):
				runs.append((run_char, run_length))
				run_char = strings[i][j + 1]
				run_length = 1
			else:
				run_length += 1
		
		string_run_lists.append(runs)
	
	mismatch = False
	
	for string_run_list in string_run_lists:
		if (len(string_run_list) != len(string_run_lists[0])):
			mismatch = True
			break

	for string_run_list in string_run_lists:
		for i in range(len(string_run_list)):
			if (string_run_list[i][0] != string_run_lists[0][i][0]):
				mismatch = True
				break
		if (mismatch):
			break
	
	if (not mismatch):
		
		min_moves = 0
		for i in range(len(string_run_lists[0])):
			
			run_length_counts = {}
			for string_run_list in string_run_lists:
				if (string_run_list[i][1] not in run_length_counts):
					run_length_counts[string_run_list[i][1]] = 1
				else:
					run_length_counts[string_run_list[i][1]] += 1
			
			most_common_run_length_count = max(run_length_counts.values())
			
			most_common_run_lengths = []
			for run_length_count in run_length_counts:
				if (run_length_counts[run_length_count] == most_common_run_length_count):
					most_common_run_lengths.append(run_length_count)
			
			most_common_run_lengths.sort()
			median_index = (len(most_common_run_lengths) - 1) / 2
			median_most_common_run_length = most_common_run_lengths[median_index]

			for string_run_list in string_run_lists:
				min_moves += abs(string_run_list[i][1] - median_most_common_run_length)
	
	sys.stdout.write('Case #' + str(case) + ': ')

	if (mismatch):
		sys.stdout.write('Fegla Won')
	else:
		sys.stdout.write(str(min_moves))

	if (case < t):
		print('')

input.close()
