def parse(text):
	lines_ = [x for x in text.split('\n') if x]
	lines = iter(lines_)
	N = int(lines.next())
	tasks = []
	for line in lines:
		n, k = line.split()
		n, k = int(n), int(k)
		tasks += [(n, k)]
	assert N == len(tasks)
	return tasks

def format(case, y, z):
	return 'Case #%d: %d %d' % (case, y, z)

def load(f):
	return parse(open(f).read())

def run(f):
	tasks = load(f)
	output = do_tasks(tasks)
	f2 = f + '.out'
	with open(f2, 'w') as fh:
		fh.write(output)
	print 'wrote output to', f2

def dec2bin(k):
	return str(bin(k))[2:]

def split(N):
	if N % 2:
		return (N - 1) / 2, (N - 1) / 2
	else:
		return (N - 1) / 2, N / 2

def locater(N, K):
	branches = dec2bin(K)
	return locate(N, branches)

def locate(N, branches):
	print 'locate:', N, branches
	if branches == '':
		return split(N)
	for branch in branches:
		Ls, Rs = split(N)
		print Ls, Rs
		# left
		if branch == '1': 
			return locate(Ls, branches[1:])
		else:
			return locate(Rs, branches[1:])

def solve(N, K):
    """overkill, finds (Ls, Rs)
    """
    rounds = len(dec2bin(K)) - 1
    A = 2**rounds - 1
    B = K - A
    space = N - A
    small_slot = (N - A) / (A + 1)
    num_big_slot = (N - A)  % (A + 1)
    if B > num_big_slot:
        Ls, Rs = split(small_slot)
    else:
        Ls, Rs = split(small_slot + 1)
    return max(Ls, Rs), min(Ls, Rs)

def do_tasks(tasks):
	output = []
	for i, (N, K) in enumerate(tasks):
		y, z = solve(N, K)
		output += [format(i+1, y, z)]
	return '\n'.join(output) + '\n'



sample_input = \
"""5
4 2
5 2
6 2
1000 1000
1000 1
"""

sample_output = \
"""Case #1: 1 0
Case #2: 1 0
Case #3: 1 1
Case #4: 0 0
Case #5: 500 499
"""

sample_tasks = parse(sample_input)
assert sample_output == do_tasks(sample_tasks)