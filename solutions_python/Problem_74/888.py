#!/usr/bin/env python


def solveCase(case):
	o_tasks = [task for task in case if task[1] == 'O']
	b_tasks = [task for task in case if task[1] == 'B']
	#print str(o_tasks)
	#print str(b_tasks)

	o_tasks_d = []
	b_tasks_d = []

	for i, t in enumerate(o_tasks):
		if i != 0:
			o_tasks_d.append([t[0], t[1], t[2], abs(o_tasks[i-1][2] - t[2])])
		else:
			o_tasks_d.append([t[0], t[1], t[2], t[2]])

	for i, t in enumerate(b_tasks):
		if i != 0:
			b_tasks_d.append([t[0], t[1], t[2], abs(b_tasks[i-1][2] - t[2])])
		else:
			b_tasks_d.append([t[0], t[1], t[2], t[2]])

	#print ''
	#print str(o_tasks_d)
	#print str(b_tasks_d)
	def findStep(step):
		for s in o_tasks_d:
			if s[0] == step: return s
		for s in b_tasks_d:
			if s[0] == step: return s
		return None
	
	step = 0
	total_distance = 0
	while (True):
		#print '======================================================================='
		#print 'step: ' + str(step)
		s = findStep(step)

		if not s:
			break

		active_task_mark = s[1]
		active_task_index= s[0]
		opposite_task_mark = 'O' if active_task_mark == 'B' else 'B'
		opposite_task_index = s[0]
		while (findStep(opposite_task_index) and findStep(opposite_task_index)[1] != opposite_task_mark):
			opposite_task_index += 1
		opposite_task = findStep(opposite_task_index)

		for t in range(active_task_index, opposite_task_index):
			curr_task = findStep(t)
			total_distance += curr_task[3] + 1
			##print 'temp total_distance: ' + str(total_distance) 
			if opposite_task:
				##print 'opposite task prije postavljanja: ' + str(opposite_task)
				opposite_task[3] = max(0, opposite_task[3] - curr_task[3] - 1)
				##print 'postavljam ot: ' + str(opposite_task[3])
				##print str(o_tasks_d)
				##print str(b_tasks_d)

		step = opposite_task_index
			
		##print str(total_distance)	
		##print '\n'

	#print 'total total distance: ' + str(total_distance)
	#print str(o_tasks_d)
	#print str(b_tasks_d)
	return total_distance - 1
		
		


input_file = open('input.txt', 'r')
cases_num = input_file.readline()
cases_num = int(cases_num)
cases = []
for index, line in enumerate(input_file.readlines()):
	line = line.strip()
	buttons_num, line = line.split(' ', 1)
	buttons_num = int(buttons_num)
	case = []
	for i in range(buttons_num):
		first, line = line.split(' ', 1)
		try:
			second, line = line.split(' ', 1)
		except:
			second = line
		case.append((i, first, int(second)))
	cases.append(case)
#print str(cases)
for i, c in enumerate(cases):
	print 'Case #' + str(i+1) + ': ' + str(solveCase(c))
