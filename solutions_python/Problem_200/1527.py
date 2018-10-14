from random import randrange
import sys
import io
import re

def problemA():
	pass

def problemB(n, case):
	j = len(n)
	print(f'Case #{case}: {n}')
	val = int(n)
	diff = 0
	if len(n) > 1:
		for i in range(1, len(n)):
			if n[i-1] > n[i]:
				diff += int(n[i:]) + 1
				break
			elif n[i-1] == n[i] and i < len(n) - 1:
				diff += int(n[i]) * (10 ** (len(n)- i - 1))
			else:
				diff = 0

		val = val - diff
		return f'Case #{case}: {val}\n'
	else:
		return f'Case #{case}: {val}\n'

if __name__ == '__main__':
	output = open(sys.argv[2], 'w')
	with open(sys.argv[1]) as f:
		i = 0
		for w in re.split('\n', f.read()):
			if i != 0:
				output.write(problemB(w, i))
			i += 1
	output.close()