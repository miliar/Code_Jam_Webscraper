from pylab import *
import sys

def handle(infile, outfile):
	line = infile.readline().split()
	n = int(line[0])
	k = int(line[1])
	m = 2**n
	rest = k % m
	if rest == m - 1:
		state = 'ON'
	else:
		state = 'OFF'
	outfile.write(' ' + state)

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1] + '.in', 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
	print 'Case #%d' % (i + 1)
	outfile.write('Case #%d:' % (i + 1))
	result = handle(infile, outfile)
	outfile.write('\n')
