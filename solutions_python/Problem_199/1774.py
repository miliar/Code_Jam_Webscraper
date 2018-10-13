import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	s = line.split(' ')[0]
	k = int(line.split(' ')[1])
	flips = 0
	
	while("-" in s and flips < 2000):
		start_index = s.index("-")
		end_index = start_index + k
		if(end_index <= len(s)):
			index = start_index
			while(index < end_index):
				if(s[index] == "-"):
					s = s[0:index] + "+" + s[(index + 1):len(s)]
				else:
					s = s[0:index] + "-" + s[(index + 1):len(s)]
				index += 1
		flips += 1
		
	if("-" in s):
		out_file.write('IMPOSSIBLE')
	else:
		out_file.write(str(flips))
	
	out_file.write('\n')

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