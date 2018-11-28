import sys, itertools

def rows(t):
	for i in xrange(4):
		yield set(t[i])

def cols(t):
	for i in xrange(4):
		yield set(t[j][i] for j in xrange(4))

def diags(t):
	yield set(t[i][i] for i in xrange(4))
	yield set(t[3-i][i] for i in xrange(4))

def main():
	case = sys.argv[1]

	with open("A-%s.in" % case, 'rb') as fin:
		with open("A-%s.out" % case, 'wb') as fout:
			n_cases = int(fin.readline().strip())
			for c in xrange(1, n_cases+1):

				t = []
				for i in xrange(4):
					t.append(fin.readline().strip())
				fin.readline()

				empties = False
				won = None

				for x in itertools.chain(rows(t), cols(t), diags(t)):
					if '.' in x: 
						empties = True
					elif 'O' not in x:
						won = 'X'
					elif 'X' not in x:
						won = 'O'

				if won is not None:
					fout.write("Case #%s: %s won\n" % (c, won))
				elif empties:
					fout.write("Case #%s: Game has not completed\n" % c)
				else:
					fout.write("Case #%s: Draw\n" % c)

if __name__ == "__main__":
	main()