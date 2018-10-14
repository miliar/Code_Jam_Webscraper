import sys

phrase = 'welcome to code jam'
#phrase = 'abc'
phraselen = len(phrase)

input = ''
inputlen = 0

counts = sys.stdin.readline().split()
N = int(counts[0])

def count_phrase(phr, inp):
	global phrase, phraselen, input, inputlen, counter
#	print '###', phrase, phraselen, input, inputlen, counter
#	print '###', phr, inp
	if phr < phraselen:
		if inp < inputlen:
			if phrase[phr] == input[inp]:
				count_phrase(phr + 1, inp + 1)
			count_phrase(phr, inp + 1)
	else:
		counter = (counter + 1) % 1000

for k in xrange(N):
	counter = 0
	input = sys.stdin.readline()
	inputlen = len(input)
	count_phrase(0, 0)
	print 'Case #%d: %04d' % (k + 1, counter)

