import sys
# import numpy as np 
# import networkx as nx
# import heapq
# import collections

INPUT_FILE = 'test.in'
OUTPUT_FILE = 'test.out'

def lv(data):
	return data.readline().rstrip('\n')

def ll(data):
	return lv(data).split(' ')

def lm(data, lines):
	src = []
	for i in range(lines):
		src.append(ll(data))
	return src

def import_file(file):
	with open(file) as data:
		T = int(lv(data))
		tests = []
		for i in range(T):
			(Ac, Aj) = [int(x) for x in ll(data)]
			ctasks = []
			for idx in range(Ac):
				(Ci, Di) = [int(x) for x in ll(data)]
				ctasks.append((Ci, Di))
			jtasks = []
			for idx in range(Aj):
				(Ci, Di) = [int(x) for x in ll(data)]
				jtasks.append((Ci, Di))
			tests.append((ctasks, jtasks))			   
		return (T, tests)

# min(x for x in my_list if x > 4)

def solution(T):
	(ctasks, jtasks) = T
	all_tasks = set([(x, 'c') for x in ctasks]) | set([(x, 'j') for x in jtasks])
	all_tasks = sorted(all_tasks, key=lambda k: k[0][1])
	cfreetime = 720 - sum([x[1] - x[0] for x in jtasks])
	jfreetime = 720 - sum([x[1] - x[0] for x in ctasks])

	one_switches = []
	two_switches = []

	new_first = ((all_tasks[0][0][0] + 1440, all_tasks[0][0][1] + 1440), all_tasks[0][1])
	all_tasks.append(new_first)

	all_tasks = sorted(all_tasks, key=lambda k: k[0][1])
	
	for idx in range(len(all_tasks) - 1):
		t1 = all_tasks[idx]
		t2 = all_tasks[idx + 1]
		if t1[1] != t2[1]:
			one_switches.append(t2[0][0] - t1[0][1])
		else:
			two_switches.append(((t2[0][0] - t1[0][1]), t1[1]))

	switches = len(one_switches)
	if all_tasks[0][1] != all_tasks[-1][1]:
		switches += 1
	
	timepool = sum(one_switches)
	two_switches = sorted(two_switches)

	for switch in two_switches:
		(duration, parent) = switch

		freetime = cfreetime if parent == 'j' else jfreetime
		otherfreetime = cfreetime if parent == 'c' else jfreetime

		if duration > freetime: 
			if freetime + timepool > duration:
				freetime = 0
				timepool = timepool - (duration - freetime)
			else:
				switches += 2
				freetime = 0
				otherfreetime = otherfreetime - duration + freetime + timepool
				timepool = 0 
		else:
			freetime = freetime - duration

		if parent == 'j':
			cfreetime = freetime
			jfreetime = otherfreetime
		else:
			cfreetime = otherfreetime
			jfreetime = freetime

	return switches

sys.stdout = open(OUTPUT_FILE, 'w')
(T, test_cases) = import_file(INPUT_FILE)
for idx in range(len(test_cases)):
	test = test_cases[idx]
	print('Case #' + str(idx + 1) + ': '), 
	print(solution(test))
	print >> sys.stderr, 'Case #' + str(idx + 1) + ': completed'