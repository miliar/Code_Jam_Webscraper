#!/usr/bin/python



def input(name):
	cases = []
	with open(name) as f:
		n = int(f.readline().strip())
		for i in xrange(n):
			data = f.readline().strip().split(' ')
			data = [int(i) for i in data]
			cases.append({
				'surprises': data[1],
				'target': data[2],
				'totals': data[3:],
			})
	return cases

def solve(case):
	case['totals'].sort(reverse=1)
	answer = 0
	for t in case['totals']:
		if t >= case['target'] * 3 - 2:
			answer += 1
		elif t >= case['target'] * 3 - 4 and case['surprises'] > 0:
			if case['target'] == 1 and t < 1:
				continue
			case['surprises'] -= 1
			answer += 1
	return answer

def output(results):
	with open('out', 'w') as f:
		for i, result in enumerate(results):
			f.write('Case #%d: %d\n' % (i+1, result))

if __name__ == '__main__':
	results = []
	for i in input('in'):
		results.append(solve(i))
	output(results)

