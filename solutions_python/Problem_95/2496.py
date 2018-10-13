inputs  = 'y e q z ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'
outputs = 'a o z q our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'

def main(line):
	o = ''
	for c in line:
		for i in xrange(len(inputs)):
			if c == inputs[i]:
				o = o + outputs[i]
				break
	return o

if __name__ == '__main__':
	import sys

#	din = [];
#	for c in map(chr, range(97, 123)):
#		if c not in inputs:
#			print c
#			
#	for c in map(chr, range(97, 123)):
#		if c not in outputs:
#			print c

	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip())
		print "Case #%d: %s" % (i + 1, res)	