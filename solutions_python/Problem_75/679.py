import sys
import re
filename = sys.argv[1]
file = open(filename, 'r')
cases = int(file.readline())
for n in range(1, cases+1):
	data = file.readline().strip('\n').split(' ')
	combine = []
	opposed = []
	sep_opp = []
	index = 0
	c = int(data[index])
	for i in range(c):
		index += 1
		combine.append([re.compile('(.*?)({}{}|{}{})(.*)'.format(data[index][0], data[index][1], data[index][1], data[index][0])), data[index][2]])
	index += 1
	c = int(data[index])
	for i in range(c):
		index += 1
		opposed.append([re.compile('.*?(({}.*?{})|({}.*?{}))'.format(data[index][0], data[index][1], data[index][1], data[index][0]))])
	large = int(data[index+1])
	cast = data[index+2]
	result = ''
	for cst in cast:
		result = result+cst
		for subst in combine:
			match = subst[0].match(result)
			if match != None:
				result = subst[0].sub('{}{}{}'.format(match.groups()[0], subst[1],match.groups()[2]), result)
		for subst in opposed:
			if subst[0].match(result):
				result = subst[0].sub('', result)
	cast_list = []
	for cst in result:
		cast_list.append(cst)
	print 'Case #{}: {}'.format(n, cast_list).replace('\'', '')