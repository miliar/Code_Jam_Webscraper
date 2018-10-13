import sys

def get_cases():
	lines = sys.stdin.read().split('\n')
	T = int(lines[0])
	cases = []
	for x in range(0,T*10,10):
		case = [map(lambda y : int(y),line.split(' ')) for line in lines[x+1:x+11]]
		trial1 = (case[0][0],case[1:5])
		trial2 = (case[5][0],case[6:])
		cases.append((trial1,trial2))
	return cases

def solve(case):
	row1_index = case[0][0]
	row2_index = case[1][0]
	row1 = case[0][1][row1_index-1]
	row2 = case[1][1][row2_index-1]
	solution = list(set(row1).intersection(set(row2)))
	if len(solution) == 1: return str(solution[0])
	elif solution: return "Bad magician!"
	else: return "Volunteer cheated!"


cases = get_cases()
for x in range(0,len(cases)):
	print "Case #" + str(x+1) + ": " + solve(cases[x])