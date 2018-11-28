import fileinput

def check(line, case_no):
	paramaters = line.split()
	
	C = float(paramaters[0])
	F = float(paramaters[1])
	X = float(paramaters[2])
	
	init_cokie_num = 2
	last_result = 0
	current_result = 0
	round = 0
	time_for_last_farm = 0
	
	while(current_result < last_result or last_result == 0):
		last_result = current_result
		productivity = init_cokie_num + F * round
		pre_time_for_last_farm = time_for_last_farm
		time_for_last_farm += C / productivity
		current_result = pre_time_for_last_farm + X / productivity
		round += 1
	print 'Case #%d: %.7f' % (case_no, last_result)
	return

indata = [line for line in fileinput.input()]
for case_no in range(1, int(indata[0])+1):
	check(indata[case_no], case_no)
