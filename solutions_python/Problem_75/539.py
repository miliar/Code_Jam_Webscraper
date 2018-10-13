import sys
def input():
	args = sys.stdin.readline()[:-1].split(' ')
	cursor = 0
	combine = {}
	if args[cursor] != '0':
		cursor += 1
		for i in range(0, len(args[cursor]), 3):
			triplet = args[cursor][i:i+3]
			combine[(triplet[0], triplet[1])] = triplet[2]
			combine[(triplet[1], triplet[0])] = triplet[2]
	cursor += 1
	oppose = []
	if args[cursor] != '0':
		cursor += 1
		for i in range(0, len(args[cursor]), 2):
			duaplet = args[cursor][i:i+2]
			oppose.append(set([duaplet[0], duaplet[1]]))
	cursor += 1
	invoke = []
	if args[cursor] != '0':
		cursor += 1
		for i in args[cursor]:
			invoke.append(i)
	return combine, oppose, invoke

def case():
	combine, oppose, invoke = input()
	element = []
	for char in invoke:
		toadd = char
		while True:
			element.append(toadd)
			if len(element) < 2:
				break
			if (element[-2], element[-1]) in combine:
				toadd = combine[(element[-2], element[-1])]
				element = element[:-2]
				continue
			for pair in oppose:
				if len(set(element) & pair) == 2:
					element[:] = []
					break
			break
	result = '['
	for char in element[:-1]:
		result += '{0}, '.format(char)
	if len(element) > 0:
		result += '{0}'.format(element[-1])
	result += ']'
	return result

n = int(sys.stdin.readline()[:-1])
for i in range(n):
	print 'Case #{0}: {1}'.format(i+1, case())

