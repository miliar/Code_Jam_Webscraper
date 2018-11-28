import sys
from collections import defaultdict
class Finish: pass
p = sys.stdout.write
T = int(raw_input())
for c in xrange(T):
	p('Case #%d: ' % (c + 1))
	on = False
	xc = defaultdict(int)
	oc = defaultdict(int)
	xd = od = 0
	xt = ot = 0

	lines = []
	while True:
		try:
			line = raw_input()
		except EOFError:
			line = ''

		if not line:
			break
		else:
			lines.append(line)

	try:
		for i in xrange(4):
			row = lines[i]
			#print row
			on = on or '.' in row
			if len(row.replace('.', '').replace('O', '')) == 4:
				p('X won')
				raise Finish
			elif len(row.replace('.', '').replace('X', '')) == 4:
				p('O won')
				raise Finish

			for j in xrange(4):
				if row[j] == 'X':
					xc[j] += 1
					if i == j:
						xd += 1
					elif i == 3 - j:
						xt += 1
				elif row[j] == 'O':
					oc[j] += 1
					if i == j:
						od += 1
					elif i == 3 - j:
						ot += 1
				elif row[j] == 'T':
					xc[j] += 1
					oc[j] += 1
					if i == j:
						xd += 1
						od += 1
					elif i == 3 - j:
						xt += 1
						ot += 1

		#print xd, xt, xc
		#print od, ot, oc
		if xd == 4 or xt == 4 or filter(lambda f: f[1] == 4, xc.items()):
			p('X won')
			raise Finish
		elif od == 4 or ot == 4 or filter(lambda f: f[1] == 4, oc.items()):
			p('O won')
			raise Finish
		if on:
			p('Game has not completed')
			raise Finish
		p('Draw')
	except Finish:
		pass
	p('\n')
