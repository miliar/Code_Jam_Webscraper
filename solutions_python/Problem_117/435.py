##libraries function
import numpy as np

##custom file name
file_n = 'B-large'

##template
input = open(file_n + '.in', 'r')
output = open(file_n + '.out', 'w')

n_case = int(input.readline())

for z in range(1, n_case+1):

	[n, m] = map(int, input.readline()[0:-1].split(' '))

	case = [[0 for i in range(m+2)]]
	for i in range(n):
		case.append([0] + map(int, input.readline()[0:-1].split(' ')) + [0])

	case.append([0 for i in range (m+2)])
	case = np.array(case)

	result = False
	for i in range(1, n+1):
		if result:
			break
		for j in range(1, m+1):
			if (case[i,:].max() <= case[i,j]) or (case[:, j].max() <= case[i,j]):
				continue
			else:
				result = 'NO'

	if not result:
		result = 'YES'

	print result
	output.write('Case #' + str(z) + ': ' + str(result) + '\n')

output.close()
