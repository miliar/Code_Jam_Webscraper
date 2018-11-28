ifile = 'A-large.in'
ofile = 'outputA_l.txt'


out = open(ofile, 'w')

def flip(row):
	for i in range(len(row)):
		if row[i] == '-':
			row[i] = '+'
		else:
			row[i] = '-'
	return row


with open(ifile, 'r') as f:
	T = int(f.readline())
	for i in range(1, T+1):
		out.write('Case #%s: ' % i)

		s, k = f.readline().split()
		s = list(s)
		k = int(k)
		l = len(s)
		count = 0

		for i in range(l-k+1):
			if s[i] == '-':
				s[i:i+k] = flip(s[i:i+k])
				count += 1
			else:
				continue

		if '-' not in s:
			out.write('%s\n' % count)
		else:
			out.write('IMPOSSIBLE\n')
		

out.close()

