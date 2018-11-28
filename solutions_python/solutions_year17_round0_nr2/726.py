from itertools import combinations_with_replacement
from operator import itemgetter

def generator():
	yield 0
	n = 1
	while True:
		for digits in combinations_with_replacement('123456789', n):
			yield int(''.join(digits))
		n += 1

def main():
	inputs = []
	cases = int(input())
	for i in range(cases):
		n = int(input())
		inputs.append((i, n))
	inputs.sort(key=itemgetter(1))
	outputs = [0] * len(inputs)
	last = None
	g = generator()
	x = next(g)
	while len(inputs) > 0:
		front = inputs[0]
		if x > front[1]:
			outputs[front[0]] = last
			inputs = inputs[1:]
		else:
			last = x
			x = next(g)
	for i in range(cases):
		print('Case #{0}: {1}'.format(i+1, outputs[i]))

if __name__ == '__main__':
	main()
