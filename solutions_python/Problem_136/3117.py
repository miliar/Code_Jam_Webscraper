from __future__ import print_function

CPS = 2.0

def main(inputf, outputf):
	if outputf == 'test.out':
		outf = file('trial.out', 'w')
	else:
		outf = file(outputf, 'w')
	
	with open(inputf, 'r') as f:
		lines = f.read().split('\n')

		for n in xrange(int(lines[0])):
			C, F, X = map(float, lines[n+1].split())

			# C=COST
			# F=ADDITIONAL CPS
			# X=target

			cps = CPS
			reinv = 0
			while True:
				produce = (X / cps) + reinv
				invest = (C / cps) + reinv + (X / (cps + F))

				if produce < invest:
					seconds = produce
					break
				else:
					reinv += (C / cps)
					cps += F

			print('Case #{:d}: {:0.7f}'.format(n + 1, seconds), file=outf)

	outf.close()

	if outputf == 'test.out':
		f1 = open('test.out', 'r')
		r1 = f1.read()
		f1.close()

		f2 = open('trial.out', 'r')
		r2 = f2.read()
		f2.close()

		if r1 != r2:
			print('FAIL {}\n{}'.format(r1, r2))
		else:
			print('pass')


if __name__ == '__main__':
	#main('test.in', 'test.out')
	main('B-large.in', 'result.out')