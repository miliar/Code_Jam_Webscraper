INPUT_FILE = 'B-large.in'
OUTPUT_FILE = 'B-large_out.txt'

def is_tidy(n):
	digs = map(lambda x : int(x), str(n))
	lastDig = 0
	for i in range(len(digs)):
		if digs[i] < lastDig:
			return False
		else:
			lastDig = digs[i]
	return True
			
def solve(f_in):
	n = int(f_in.readline().strip())
	while not is_tidy(n):
		digs = map(lambda x : int(x), str(n))
		firstG = 0
		for i in range(1, len(digs)):
			if digs[i] < digs[i-1]:
				firstG = i-1
				break
		digs[firstG] = digs[firstG] - 1
		for i in range(firstG + 1, len(digs)):
			digs[i] = 9
		nStr = ''
		for i in range(len(digs)):
			nStr = nStr + str(digs[i])
		n = int(nStr)
	return n
with open(INPUT_FILE, 'r') as f:
	with open(OUTPUT_FILE, 'w') as f_out:
		T = int(f.readline())
		for i in range(T):
			f_out.write('Case #%d: %s\n'%(i + 1, solve(f)))
				