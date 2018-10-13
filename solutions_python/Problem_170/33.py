#!/usr/bin/python3

import sys
from concurrent.futures import ProcessPoolExecutor

def ans(inputs):
	english = inputs[0]
	french = inputs[1]
	either = inputs[2]
	#print("english: {0}".format(english))
	#print("french: {0}".format(french))
	#print("either: {0}".format(either))

	least = float("inf")
	num = len(either)
	sent = 2**num
	for i in range(sent):
		e = set(english)
		f = set(french)

		mask = bin(i + sent)[3:]
		for j in range(num):
			if mask[j] == '0':
				e.update(either[j])
			else:
				f.update(either[j])

		size = len(e.intersection(f))
		least = min(size, least)
	
	return least

if __name__ == "__main__":
	lines = int(sys.stdin.readline())

	inputs = []
	for i in range(lines):
		total = int(sys.stdin.readline())
		english = sys.stdin.readline().split()
		french = sys.stdin.readline().split()
		either = []
		for j in range(total-2):
			tmp = sys.stdin.readline().split()
			either.append(tmp)

		inputs.append((english, french, either))
	with ProcessPoolExecutor(max_workers = 6) as executor:
			outputs = executor.map(ans, inputs)

	output = list(outputs)
	for i in range(lines):
		print("Case #{0}: {1}".format(str(i+1), output[i]))
