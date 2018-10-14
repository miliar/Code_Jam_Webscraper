INPUT_FILE = 'A-large.in'
OUTPUT_FILE = 'A-large_out.txt'

def solve(f_in):
	l = f_in.readline().strip()
	lst = l.split(' ')
	k = int(lst[1])
	pancakesStr = lst[0]
	pancakes = 0
	nPancakes = len(pancakesStr)
	for i in range(nPancakes):
		if pancakesStr[i] == '-':
			pancakes = pancakes | (1 << (nPancakes - i - 1))
	countFlips = 0
	flip = 0
	for i in range(k):
		flip = flip | (1 << i)
	for i in range(nPancakes - k + 1):
		if pancakes & (1 << (nPancakes - i - 1)):
			countFlips = countFlips + 1
			pancakes = pancakes ^ (flip << nPancakes - k - i)
	if pancakes == 0:
		result = countFlips
	else:
		result = "IMPOSSIBLE"
	return result

with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n' % (i + 1, solve(f)))
				