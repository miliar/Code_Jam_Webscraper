import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	s = in_file.readline().replace('\n', '')
	# Look for 'Z' for zeroes
	# 'W' for twos
	# 'G' for eights
	# 'U' for fours
	# 'X' for sixes
	# 'T' has to be threes after the others are finished
	# 'F' has to be fives after the others are finished
	# 'O' has to be ones after the others are finished
	# 'S' has to be sevens after the others are finished
	# 'N' has to be nines after the others are finished
	zeroes = s.count('Z')
	twos = s.count('W')
	eights = s.count('G')
	fours = s.count('U')
	sixes = s.count('X')
	threes = s.count('T') - twos - eights
	fives = s.count('F') - fours
	ones = s.count('O') - zeroes - twos - fours
	sevens = s.count('S') - sixes
	nines = (s.count('N') - ones - sevens) / 2
	
	out = ""
	i = 0
	while (i < zeroes):
		i += 1
		out += "0"
	i = 0
	while (i < ones):
		i += 1
		out += "1"
	i = 0
	while (i < twos):
		i += 1
		out += "2"
	i = 0
	while (i < threes):
		i += 1
		out += "3"
	i = 0
	while (i < fours):
		i += 1
		out += "4"
	i = 0
	while (i < fives):
		i += 1
		out += "5"
	i = 0
	while (i < sixes):
		i += 1
		out += "6"
	i = 0
	while (i < sevens):
		i += 1
		out += "7"
	i = 0
	while (i < eights):
		i += 1
		out += "8"
	i = 0
	while (i < nines):
		i += 1
		out += "9"
	
	out_file.write(out)
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