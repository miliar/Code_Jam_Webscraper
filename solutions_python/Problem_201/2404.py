import sys

def load(infile):
	with open(infile, 'r') as f:
		infile = f.read().splitlines()[1:]
	
	return [x.split() for x in infile]

def comparator(x, y):
	sz_x = x[1] - x[0]
	sz_y = y[1] - y[0]
	if sz_x != sz_y:
		return cmp(sz_y, sz_x)
	return cmp(x[0], y[0])

def run_test(case):
	gaps = [(0, int(case[0]) - 1)]
	for i in range(int(case[1]) - 1):
		sz = gaps[0][1] - gaps[0][0] + 1
		cut_elem = (sz / 2) - (1 - sz % 2)
		gap = gaps.pop(0)
		if cut_elem != 0:
			gaps.append((gap[0], gap[0] + cut_elem - 1))
		gaps.append((gap[0] + cut_elem + 1, gap[1]))
		gaps.sort(cmp = comparator)
	#print(gaps)
	sz = gaps[0][1] - gaps[0][0] + 1
	cut_elem = (sz / 2) - (1 - sz % 2)
	r = sz - cut_elem - 1
	return max(cut_elem, r), min(cut_elem, r)
	
def _main(infile):
	cases = load(infile)
	i = 1
	for case in cases:
		y, z = run_test(case)
		print('Case #{0}: {1} {2}'.format(i, y, z))
		i += 1

if __name__ == "__main__":
	_main(sys.argv[1])
