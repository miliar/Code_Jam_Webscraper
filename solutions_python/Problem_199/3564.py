def flip(string, start, end):
	temp = list(string)
	for i in range(start, end, 1):
		if temp[i] == '+':
			temp[i] = '-'
		elif temp[i] == '-':
			temp[i] = '+'
		result = ''.join(temp)
	return result

casenum = int(input())
case = ''
resultlist = []
for i in range(casenum):
	caselist = input().split(' ')
	case = caselist[0]
	flipper = int(caselist[1])
	result = 0
	count = 0
	
	if len(case) >= flipper:
		if '-' not in list(case):
			result = 0
		else:
			for j in range(len(case)):
				if case[j] == '-' and (j+flipper) <= len(case):
					case = flip(case, j, (j+flipper))
					result += 1
			if '-' in case:
				result = 'IMPOSSIBLE'

	caseName = 'Case #' + str(i+1) + ': ' + str(result)
	resultlist.append(caseName)

for s in resultlist:
	print(s)
	

