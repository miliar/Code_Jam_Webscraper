from sys import stdin
from itertools import islice, izip_longest, tee

def parse_input(inFile):
	for line in islice(inFile, 1, None):
		yield parse_line(line)

def parse_line(line):
	tokens = line.split()

	num_combis = int(tokens.pop(0))

	combis = tokens[:num_combis]
	tokens = tokens[num_combis:]
	
	num_opposed = int(tokens.pop(0))

	oppositions = tokens[:num_opposed]
	tokens = tokens[num_opposed:]

	elements = tokens[1]

	return parse_combis(combis), parse_oppositions(oppositions), elements

def parse_combis(combis):
	d = {}
	for combi in combis:
		d[frozenset(combi[:2])] = combi[2]
	return d

def parse_oppositions(oppositions):
	d = {}
	for opp in oppositions:
		a = opp[0]
		b = opp[1]
		d[a] = b
		d[b] = a
	return d

def process_elements(elements, combis, oppositions):
	out = []
	for i in elements:
		if out:
			combi = frozenset((i, out[-1]))
			if combi in combis:
				out = out[:-1]
				i = combis[combi]

		if i in oppositions and oppositions[i] in out:
			out = []
		else:
			out.append(i)
	return out

for test, (combis, opps, elements) in enumerate(parse_input(stdin)):
	out = process_elements(elements, combis, opps)

	print 'Case #%d: %s' % (test + 1, '['+', '.join(out) +']')
