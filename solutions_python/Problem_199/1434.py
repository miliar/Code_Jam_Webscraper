from random import randrange
import sys
import io
import re

def problemA(n, k, case):
	#n = re.sub(r"-", "0", re.sub(r"\+", "1", n))
	#print(bin(int(n, 2)))
	count = 0
	for i in range(len(n)):
		if n[i] == "-" and i+k <= len(n):
			count += 1
			for j in range(k):
				if n[i+j] == "+":
					n[i+j] = "-"
				else:
					n[i+j] = "+"
			i = k + i
	if "-" in n:
		return f'Case #{case}: IMPOSSIBLE\n'
	else:
		return f'Case #{case}: {count}\n'

def flip(n, k):
	for i in range(k):
		if n[i] == "+":
			n[i] = "-"
		else:
			n[i] = "+"
	return n

def problemB(n, case):
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
			x = re.split('\s', w)
			if i != 0:
				output.write(problemA(list(x[0]), int(x[1]), i))
			i += 1
	output.close()