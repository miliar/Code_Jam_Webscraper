import sys
import os

T = int(sys.stdin.readline())

rules = {
	('1','1'):('1','0'),
	('1','i'):('1','i'),
	('1','j'):('1','j'),
	('1','k'):('1','k'),

	('i','1'):('1','i'),
	('i','i'):('-1','0'),
	('i','j'):('1','k'),
	('i','k'):('-1','j'),

	('j','1'):('1','j'),
	('j','i'):('-1','k'),
	('j','j'):('-1','0'),
	('j','k'):('1','i'),

	('k','1'):('1','k'),
	('k','i'):('1','j'),
	('k','j'):('-1','i'),
	('k','k'):('-1','0'),
}

for t in xrange(T):
	L, X = map(int, sys.stdin.readline().strip().split())
	lstring = sys.stdin.readline().strip()

	#print L, X, lstring
	result = ('1', '0')
	ifound = jfound = False

	for i in xrange(X):
		for c in lstring:
			if result[1] == '0':
				result = (result[0], c)
			else:
				a, b = rules[(result[1], c)]
				result = (str(int(result[0])*int(a)), b)

			if not ifound and result[0] == '1' and result[1] == 'i':
				ifound = True
			elif ifound and result[0] == '1' and result[1] == 'k':
				jfound = True

	if ifound and jfound and result[0] == '-1' and result[1] == '0':
		finalresult = 'YES'
	else:
		finalresult = 'NO'

	sys.stdout.write('Case #{0}: {1}\n'.format(t+1, finalresult))



