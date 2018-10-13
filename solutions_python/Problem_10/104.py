import sys


def process_case(P, K, L, freq):
	minfreq = 0
	freq.sort()
	freq.reverse()

	for i in xrange(L):
		minfreq += freq[i] * (i / K + 1)

	return minfreq


def fread():
	try:
		inp = open(sys.argv[1], 'rt')
	except IOError:
		print 'Invalid input filename'
		sys.exit(2)

	out = open(sys.argv[2], 'wt')

	ncases = int(inp.readline())

	for i in xrange(ncases):
		print i
		P, K, L = map(int, inp.readline().split())
		freq = list(map(int, inp.readline().split()))
		out.write('Case #%d: %d\n' % (i + 1, process_case(P, K, L, freq)))

	inp.close()
	out.close()



if __name__ == '__main__':
#	print process_case(3, 9, 26, [1, 1, 1, 100, 100, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 11, 11, 11, 11, 1, 1, 1, 100])
	fread()
