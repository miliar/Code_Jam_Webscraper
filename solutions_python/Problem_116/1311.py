import fileinput

def subcheck(item):
	count_o = item.count('O')
	count_x = item.count('X')
	count_t = item.count('T')
	if count_o + count_t == 4:
		return 'O'
	elif count_x + count_t == 4:
		return 'X'
	else:
		return ''

def check(acase, case_no):
	for line in acase:
		checkresult = subcheck(line);
		if checkresult != '':
			print 'Case #%d: %s won' % (case_no, checkresult)
			return

	acase = [''.join([item[i] for item in acase]) for i in range(4)]
	for row in acase:
		checkresult = subcheck(row);
		if checkresult != '':
			print 'Case #%d: %s won' % (case_no, checkresult)
			return

	checkresult = subcheck(''.join([item[i] for (i, item) in enumerate(acase)]));
	if checkresult != '':
		print 'Case #%d: %s won' % (case_no, checkresult)
		return
	
	checkresult = subcheck(''.join([item[3-i] for (i, item) in enumerate(acase)]));
	if checkresult != '':
		print 'Case #%d: %s won' % (case_no, checkresult)
		return

	if (''.join(acase)).count('.') == 0:
		print 'Case #%d: Draw' % case_no
	else:
		print 'Case #%d: Game has not completed' % case_no


indata = [line for line in fileinput.input()]
cases = int(indata[0])
line_no = 1

for case_no in range(cases):
	acase = indata[line_no:(line_no+4)]
	check(acase, case_no+1)
	line_no = line_no + 5
