debug_print = False
attempt = 'l0'

def debug(st):
	if debug_print:
		print st

f = open(attempt + '.in', 'r')
num_cases = int(f.readline())

for case_num in range(1, num_cases+1):
	rc = f.readline().split()
	r = int(rc[0])
	c = int(rc[1])

	possible = True

	ls = []
	for rr in range(r):
		ls.append(f.readline().strip())

	debug('%d %d %s' % (r, c, str(ls)))

	for j in range(len(ls)):
		ls0 = []		
		for c in ls[j]:
			ls0.append(c)
		ls1 = []

		last_row = False
		if j == len(ls)-1:
			last_row = True
		else:
			for c in ls[j+1]:
				ls1.append(c)	
		
		for i in range(len(ls0)):
			c = ls0[i]

			last_col = False
			if i == len(ls0)-1:
				last_col = True

			if c == '.':
				continue
			if c == '#':
				ls0[i] = '/'
				if not last_col and ls0[i+1] == '#':
					ls0[i+1] = '\\'
				else:
					possible = False

				if not last_row and ls1[i] == '#':
					ls1[i] = '\\'
				else:
					possible = False

				if not last_col and not last_row and ls1[i+1] == '#':
					ls1[i+1] = '/'
				else:
					possible = False

			ls[j] = ''.join(ls0)
			if not last_row:
				ls[j+1] = ''.join(ls1)
				
	out = ''
	if possible:
		for lss in ls:
			out += '\n' + lss
	else:
		out += '\nImpossible'
	print 'Case #%d:%s' % (case_num, out)

f.close()
