def strint_to_list(string):
	output = []
	for i in string:
		output.append(i)
	return output

def fun():
	R, C = map(int, raw_input().split())
	dimen = []
	for i in xrange(R):
		dimen.append(strint_to_list(raw_input()))


	while 1 == 1:
		finish = 1
		for line in dimen:
			if '#' in line:
				finish = 0
				break
		if finish == 1:
			return dimen
		else:
			for i in xrange(R):
				for j in xrange(C):
					if dimen[i][j] == '#':
						if i + 1 == R or j + 1 == C:
							return 'im'
						else:
							a = dimen[i][j]
							b = dimen[i][j+1]
							c = dimen[i + 1][j]
							d = dimen[i + 1][j+1]
							if a == '#' and b == '#' and c =='#' and d == '#':
								dimen[i][j] = '/'
								dimen[i][j+1] = '\\'
								dimen[i+1][j] = '\\'
								dimen[i+1][j+1] = '/'
							else:
								return 'im'
numCase = input()
for round in xrange(numCase):
	print 'Case #%d:' % (round + 1)
	out = fun()
	if out == 'im':
		print 'Impossible'
	else:
		for line in out:
			pp = ''
			for co in line:
				pp += co
			print pp
				