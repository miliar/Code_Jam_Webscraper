import fileinput

indata = [line for line in fileinput.input()]
cases = int(indata[0])
line_no = 1

for case_no in range(1, cases+1):
	answer1 = int(indata[line_no])
	arrangement1 = indata[line_no+1:(line_no+1+4)]
	answer2 = int(indata[line_no+5])
	arrangement2 = indata[line_no+5+1:(line_no+5+1+4)]
	
	answer1_set = set(arrangement1[answer1-1].split())
	answer2_set = set(arrangement2[answer2-1].split())
	
	result_set = answer1_set.intersection(answer2_set)
	
	result_set_len = len(result_set)
	if result_set_len == 0:
		print 'Case #%d: Volunteer cheated!' % (case_no)
	elif result_set_len == 1:
		print 'Case #%d: %s' % (case_no, result_set.pop())
	else:
		print 'Case #%d: Bad magician!' % (case_no)
	
	line_no += 10