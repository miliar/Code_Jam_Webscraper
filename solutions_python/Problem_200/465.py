def dropposition(number):
	l = len(number)
	k = 0
	while k < l-1 and int(number[k+1]) >= int(number[k]):
		k += 1
	if k == l-1:
		return k
	while k > 0 and int(number[k-1]) == int(number[k]):
		k -= 1
	return k

def tidify(number):
	d = dropposition(number)
	l = len(number)
	if d == l-1:
		return number
	if d == 0 and number[d] == '1':
		return '9'*(l-1)
	else:
		return number[:d] + str(int(number[d])-1) + '9'*(l-d-1)

import sys
with open(sys.argv[1], "r") as fileIN:
	inputLines = fileIN.readlines()
		
with open(sys.argv[2], "w") as fileOUT:
	numberOfCases = int(inputLines.pop(0))
	for num in range(numberOfCases):
		number = inputLines.pop(0).rstrip()
		fileOUT.write('Case #' + str(num+1) + ': ' + tidify(number) + '\n')