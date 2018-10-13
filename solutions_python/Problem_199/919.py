import sys

def flip(pans, f_size, start_ind):
	out = pans[:start_ind]
	for i in xrange(start_ind, start_ind + f_size):
		if pans[i] == '+':
			out += '-'
		else:
			out += '+'
	return out + pans[start_ind + f_size:]

def solve(pans, f_size, start_ind=0):
	if '-' not in pans:
		return 0

	if pans[start_ind] == '-':
		try:
			return solve(flip(pans, f_size, start_ind), f_size, start_ind + 1) + 1
		except:
			return 'IMPOSSIBLE'
	else:
		return solve(pans, f_size, start_ind + 1)

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		pans, f_size = lines.pop(0).strip().split(' ')
		res = solve(pans, int(f_size))
		print 'Case #%d: %s' % (i + 1, res)
		outfile.write('Case #%d: %s\n' % (i + 1, res))
