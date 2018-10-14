from parser import parse
from collections import defaultdict

wins = [(0,1,2,3), (4,5,6,7), (8,9,10,11), (12,13,14,15),
	    (0,4,8,12), (1,5,9,13), (2,6,10,14), (3,7,11,15),
	    (0,5,10,15), (3,6,9,12)]

def helper(test):
	d = defaultdict(list)
	rows = test[:4]
	game = rows[0] + rows[1] + rows[2] + rows[3]
	for i,a in enumerate(game):
		d[a].append(i)
	for player,positions in d.items():
		if player in ['.', 'T']:
			continue
		positions = positions + d['T']
		for win in wins:
			if all([b in positions for b in win]):
				return '{} won'.format(player)
	return 'Game has not completed' if '.' in d.keys() else 'Draw'

schema = [(),[str,str,str,str,str]]
num_tests,tests = parse(schema)
for case,test in enumerate(tests):
	sol = helper(test)
	print 'Case #{}: {}'.format(case+1, sol)
