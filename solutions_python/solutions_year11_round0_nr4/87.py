import operator
import os.path
import sys

debug = 0

which = sys.argv[1]
dir = os.path.dirname(__file__)
fname = os.path.join(dir, which)
assert os.path.exists(fname+".in")

def test(elems):
	elems = [x-1 for x in elems]
	handled = [False] * len(elems)
	numHits = float(0)
	for i in xrange(len(elems)):
		if handled[i]:
			continue
		handled[i] = True
		numInGroup = 1
		j = elems[i]
		while j != i:
			handled[j] = True
			numInGroup += 1
			j = elems[j]

		if numInGroup > 1:
			numHits += float(numInGroup)
	return numHits

def go():
	with open(fname + '.in') as f_in:
		lines = f_in.readlines()
	with open(fname + '.out', 'w') as f_out:
		numTests = int(lines.pop(0))
		case = 0
		while numTests:
			numTests -= 1
			case += 1

			N = int(lines.pop(0))
			assert N >= 1
			elems = [int(x) for x in lines.pop(0).strip().split(' ')]
			assert len(elems) == N

			result = test(elems)

			outline = 'Case #%s: %s' % (case, result)
			print outline
			f_out.write(outline + '\n')

		assert not lines or lines == ['']

go()
