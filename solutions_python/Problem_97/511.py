from datetime import datetime
def solve(line):
	numbers = [int(x) for x in line.split(' ')]
	A = numbers[0]
	B = numbers[1]
	total = 0
	for n in range(A, B):
		s = str(n)
		d = []
		for j in range(len(s)):
			if int(s[j]) > 0:
				m = int(s[j:] + s[0:j])
				if n < m and m <= B and m not in d:
					total += 1
					d.append(m)
	return total

start = datetime.now()

with open('large.in', 'rb') as fin:
	with open('large.out', 'wb') as fout:
		total_lines = int(fin.readline())
		for i in range(1, total_lines + 1):
			fout.write('Case #%s: %s\n' % (i, solve(fin.readline())))
			fout.flush()

print((datetime.now() - start))