##libraries function
import numpy as np

##custom file name
file_n = 'A-large'

##template
input = open(file_n + '.in', 'r')
output = open(file_n + '.out', 'w')

n_case = int(input.readline())

def readline(line):
	full = False
	winner = None
	if '.' not in line:
		full = True
	else:
		return full, winner
	if 'X' not in line:
		winner = 'O'
	if 'O' not in line:
		winner = 'X'
	return full, winner

for z in range(1, n_case+1):
    
    case = []
    for k in range(4):
    	case.append([i for i in input.readline() if i != '\n'])

    input.readline()

    case = np.array(case)
    t_full = 0
    result = None
    for k in range(4):
    	full, winner = readline(case[k])
    	if winner:
    		result = winner + ' won'
    		break
    	t_full += full

    if not result:
    	for k in range(4):
			full, winner = readline(case[:,k])
			if winner:
				result = winner + ' won'
				break
			t_full += full

	if not result:
		for k in [[case[i][i] for i in range(4)], [case[i][(-1-i)%4] for i in range(4)]]:
			full, winner = readline(k)
			if winner:
				result = winner + ' won'
				break
			t_full += full

	if not result:
		if t_full == 10:
			result = 'Draw'
		else:
			result = 'Game has not completed'
    
    output.write('Case #' + str(z) + ': ' + str(result) + '\n')

output.close()