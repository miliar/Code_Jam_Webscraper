fin = open('A-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for c in xrange(t):
	s, k = fin.readline().split()
	chars = []
	chars.extend(s)
	print chars
	k = int(k)
	flips = 0
	for i in xrange(len(s) - k + 1):
		if chars[i] == '-':
			flips += 1
			for j in xrange(k):
				if chars[i + j] == '+':
					chars[i + j] = '-'
				else:
					chars[i + j] = '+'
	possible = True	
	for i in xrange(k):
		if chars[-1 - i] == '-':
			possible = False
			break
	if possible:
		fout.write('Case #' + str(c + 1) + ': ' + str(flips) + '\n')
	else:
		fout.write('Case #' + str(c + 1) + ': IMPOSSIBLE\n')

fout.close()
