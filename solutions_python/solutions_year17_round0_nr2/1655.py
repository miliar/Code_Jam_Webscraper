fin = open('B-large.in', 'r')
fout = open('output.txt', 'w')

t = int(fin.readline())

for c in xrange(t):
	n = int(fin.readline())
	n = str(n)
	l = []
	l.extend(n)
	reduced = False
	i = 0
	while i < len(n):
		if reduced:
			l[i] = '9'
		elif i < len(n) - 1:
			if l[i] > l[i + 1]:
				while i >= 0:
					l[i] = str(int(l[i]) - 1)
					if i == 0 or l[i - 1] <= l[i]:
						break
					i -= 1
				if i < 0:
					i = 0
				reduced = True
		i += 1
	answer = int(''.join(l))

	fout.write('Case #' + str(c + 1) + ': ' + str(answer) + '\n')

fout.close()
