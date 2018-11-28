import operator
import os.path
import sys

debug = 0

which = sys.argv[1]
dir = os.path.dirname(__file__)
fname = os.path.join(dir, which)
assert os.path.exists(fname+".in")


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
			assert N >= 2
			candies = [int(x) for x in lines.pop(0).strip().split(' ')]
			assert len(candies) == N

			if reduce(operator.xor, candies) != 0:
				outline = 'Case #%s: NO' % case
				print outline
				f_out.write(outline + '\n')
				continue

			remaining = sum(candies) - min(candies)

			outline = 'Case #%s: %s' % (case, remaining)
			print outline
			f_out.write(outline + '\n')

		assert not lines or lines == ['']

go()
