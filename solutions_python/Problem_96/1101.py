def compute(data):
	[N, S, p] = [int(d) for d in data[0:3]]
	if not 1 <= N <= 100 or not 0 <= S <= N or not 0 <= p <= 10:
		return
	t         = [int(d) for d in data[3:(3 + N)]]
	for score in t:
		if not 0 <= score <= 30:
			return
	ns_score = p * 1 + max((p - 1), 0) * 2
	s_score  = p * 1 + max((p - 2), 0) * 2
	y = 0
	rest = []
	for i in range(len(t)):
		if t[i] >= ns_score:
			y += 1
		else:
			rest += [t[i]]
	s = 0
	for score in rest:
		if s >= S:
			break
		elif score >= s_score:
			y += 1
			s += 1
	return y

def solve(input):
	data = input.split('\n')
	T = int(data.pop(0))
	if not 1 <= T <= 100:
		return
	data = data[0:T]
	output = ''
	for x in range(len(data)):
		#######
		y = compute(data[x].split(' '))
		#######
		output += 'Case #%d: %d' % (x + 1, y) + '\n'
	return output

import sys
if len(sys.argv) > 1:
	with open(sys.argv[1]) as f:
		input = f.read()
	output = solve(input)
	print output
	if len(sys.argv) > 2:
		with open(sys.argv[2], 'w') as f:
			f.write(output)