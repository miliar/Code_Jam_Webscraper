
import fractions

f = open('/Users/Wanli/Downloads/A-large.in.txt')
# f = open('pinput.txt')
ncases = int(f.readline())

for case in range(ncases):
	tokens = f.readline().strip().split('/')
	a0 = int(tokens[0])
	b0 = int(tokens[1])

	a = a0 / fractions.gcd(a0, b0)
	b = b0 / fractions.gcd(a0, b0)

	counter = 0
	flag = True

	d = b
	while d > 1:
		if d % 2 != 0:
			flag = False
		d /= 2

	while a < b and flag:
		if b % 2 != 0:
			flag = False
			break
		b /= 2
		counter += 1

	if not flag:
		print 'Case #%d: impossible' % (case+1)
	else:
		print 'Case #%d: %d' % (case+1, counter)
