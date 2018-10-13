
def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item

def np(a):
    return ' '.join([str(x) for x in a])

def main(line):
        N = int(line[0])
        s = [int(x) for x in line[1:]]
        h = dict()
        for x in powerset(s):
            if len(x) < 1: continue
            v = sum(x)
            # print x, sum
            if v in h:
                return '\n'+np(x)+'\n'+np(h[v])
            h[v] = x
        return 'Impossible'

if __name__ == '__main__':
	import sys
	N = int(sys.stdin.readline())
	for i in xrange(N):
		res = main(sys.stdin.readline().strip().split(' '))
		print "Case #%d: %s" % (i + 1, res)	

