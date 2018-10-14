import fileinput
import math

def readline(inp):
	return map(int, inp.readline().strip().split(' '))

pals = []
for i in xrange(1, int(1.e7+1)):
	num = str(i)
	num2 = str(i*i)
	if (num == num[::-1]) and (num2 == num2[::-1]):
		pals.append(i*i)

inp = fileinput.input()
(t,) = readline(inp)
for i in xrange(1, t+1):
	(a, b) = readline(inp)
	print 'Case #{0}: {1}'.format(i, sum(1 for p in pals if a <= p <= b))
inp.close()