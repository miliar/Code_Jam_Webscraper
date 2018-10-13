import sys

def solve(in_file, out_file, case):
	out_file.write('Case #' + str(case + 1) + ': ')
	
	line = in_file.readline().replace('\n', '')
	d_distance = int(line.split(' ')[0])
	n_horses = int(line.split(' ')[1])
	
	#horses = []
	max_time = 0
	i = 0
	while(i < n_horses):
		#horse_data = []
		line = in_file.readline().replace('\n', '')
		k_start_distance = int(line.split(' ')[0])
		s_max_speed = int(line.split(' ')[1])
		time = (d_distance - k_start_distance) / float(s_max_speed)
		if time > max_time:
			max_time = time
		#horse_data.append(k_start_distance)
		#horse_data.append(s_max_speed)
		#horses.append(horse_data)
		i += 1
	
	out_file.write(str(float(d_distance) / max_time))
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