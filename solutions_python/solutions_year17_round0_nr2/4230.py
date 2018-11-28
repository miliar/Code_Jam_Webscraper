def istidy(number):
	for i in range(len(number)-1):
		if number[i] > number[i+1]:
			return False
	return True

casecount = int(input())
list = []
for i in range(casecount):
	number = int(input())

	for i in range(number,0,-1):
		if istidy(str(i)):
			list.append(i)
			break

for i in range(casecount):
	caseName = 'Case #' + str(i+1) + ': '
	print(caseName + str(list[i]))
