import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	n = line
	
	while(tidy_index(n) != len(n)):
		if(tidy_index(n) == 1 and n[0] == '1'):
			new_n = ""
			index = 0
			while(index < (len(n) - 1)):
				new_n += "9"
				index += 1
			n = new_n
		else:
			t_index = tidy_index(n)
			n = n[0:t_index - 1] + str(int(n[t_index - 1]) - 1) + n[t_index:len(n)]
			new_n =  n[0:t_index]
			index = t_index
			while(index < len(n)):
				new_n += "9"
				index += 1
			n = new_n
	
	out_file.write(n)
	out_file.write('\n')

def tidy_index(number_string):
	if(len(number_string) > 1):
		lowest = int(number_string[len(number_string) - 1])
		index = len(number_string) - 2
		while(index >= 0):
			newest = int(number_string[index])
			if(newest > lowest):
				return index + 1
			lowest = newest
			index -= 1
	return len(number_string)
	
if len(sys.argv) != 2:
	print 'Please provide one parameter with the name of the input file location relative to this file.'
else:
	in_file = open(str(sys.argv[1]), 'r')
	out_file = open(str(sys.argv[1]).replace('.in', '.out'), 'w')
	cases = int(in_file.readline())
	case = 0
	while (case < cases):
		solve(in_file, out_file, case)
		case += 1
	in_file.close()
	out_file.close()