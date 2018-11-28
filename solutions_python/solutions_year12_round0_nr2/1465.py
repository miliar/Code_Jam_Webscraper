#!/usr/bin/python

def best(case):
	"""case[0] = nb of googlers
	case[1] = nb of surprising results
	case[2] = at_least"""
	count=0
	googlers=case[3:]
	googlers.sort(reverse=True)

	if case[2] >=2:
		best_surprising = case[2] + 2*(case[2]-2)
		best_normal = case[2]+2*(case[2]-1)
	else:
		best_normal = case[2]
		best_surprising = case[2]
	
	while case[1] > 0:
		try:
			if googlers.pop() >= best_surprising:
				case[1]-=1
				count+=1
		except:
			break
	while len(googlers) >0:
		if googlers.pop() >= best_normal:
			count+=1
	return count


nb_lines = int(input())
cases=list()
for j in range(nb_lines):
	cases.append([int(i) for i in input().split()])

for i in range(nb_lines):
	print('Case #' + str(i+1) + ': ' + str(best(cases[i])))
