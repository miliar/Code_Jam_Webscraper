import os.path
import sys

debug = 0

which = sys.argv[1]
dir = os.path.dirname(__file__)
fname = os.path.join(dir, which)
assert os.path.exists(fname+".in")

baseelems = "QWERASDF"
elemlist = []
combiners = {}
opposed = {}

def invoke(x):
	global elemlist

	# combine
	if elemlist:
		possibleCombine = elemlist[-1] + x
		if possibleCombine in combiners:
			elemlist[-1] = combiners[possibleCombine]
			return

	# oppose
	if elemlist and x in opposed:
		for y in opposed[x]:
			if y in elemlist:
				elemlist = []
				return

	elemlist.append(x)

def go():
	global elemlist
	global combiners
	global opposed

	with open(fname + '.in') as f_in:
		lines = f_in.readlines()
	with open(fname + '.out', 'w') as f_out:
		numTests = int(lines[0])
		for case, line in enumerate(lines[1:]):
			elemlist = []
			combiners = {}
			opposed = {}

			if debug >= 10: print line
			specs = line.strip().split(' ')
			C = int(specs.pop(0))
			assert not combiners
			while C:
				chars = specs.pop(0)
				if debug >= 10: print 'C', chars
				combiners[chars[0] + chars[1]] = chars[2]
				combiners[chars[1] + chars[0]] = chars[2]
				C -= 1
			D = int(specs.pop(0))
			assert not opposed
			while D:
				chars = specs.pop(0)
				if debug >= 10: print 'D', chars
				for c in chars:
					if c not in opposed:
						opposed[c] = set()
				opposed[chars[0]].add(chars[1])
				opposed[chars[1]].add(chars[0])
				D -= 1
			N = int(specs.pop(0))
			chars = specs.pop(0)
			if debug >= 10: print 'N', chars
			assert len(specs) == 0
			assert len(chars) == N, "chars: %s, N: %s" % (chars, N)
			if debug >= 10: print

			elemlist = []
			for n in chars:
				invoke(n)
			outline = 'Case #%s: [%s]' % (case+1, ', '.join(elemlist))
			if debug:
				print line.strip() + (' ' * (25-len(line.strip()))),
			print outline
			f_out.write(outline + '\n')
go()
