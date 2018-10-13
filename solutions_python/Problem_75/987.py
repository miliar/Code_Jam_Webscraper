from operator import itemgetter, attrgetter
import os, logging

FILE = 'B-large'

if __name__ == "__main__":
	import doctest, Magicka
	doctest.testmod(Magicka)


def runner():
	path = os.path.join(os.path.dirname(__file__), 'input', '%s.in.txt' % FILE)
	f = open(path, 'r')
	
	path = os.path.join(os.path.dirname(__file__), 'output', '%s.out.txt' % FILE)
	r = open(path, 'w')
	
	for n, test_case in enumerate(f.readlines()[1:]):
		r.write('Case #%r: [%s]\n' % (n+1, ', '.join(magicka(test_case))))
	
	f.close()
	r.close()
	
	
def magicka(test_case):
	'''
	>>> magicka('0 0 2 EA')
	['E', 'A']
	
	>>> magicka('1 QRI 0 4 RRQR')
	['R', 'I', 'R']
	
	>>> magicka('1 QFT 1 QF 7 FAQFDFQ')
	['F', 'D', 'T']

	>>> magicka('1 EEZ 1 QE 7 QEEEERA')
	['Z', 'E', 'R', 'A']

	>>> magicka('3 EEZ FER ART 1 QE 7 QEEEERA')
	['Z', 'E', 'R', 'A']
	
	>>> magicka('0 1 QW 2 QW')
	[]
	'''
	
	l = test_case.split()
	C = int(l[0])

	forms = {}
	
	for i in xrange(1, C+1):
		setup = l[i]
		forms[(setup[0], setup[1])] = setup[2]
		forms[(setup[1], setup[0])] = setup[2]

	D = int(l[1+C])
	
	opposed = []
	
	for i in xrange(2+C, 2+C+D):
		setup = l[i]
		opposed.append((setup[0], setup[1]))
	
	invoke = l.pop()

	logging.warning('%s %s %s %s' % (test_case, forms, opposed, invoke))

	queue = []
	for elem in invoke:
		queue.append(elem)
		if len(queue) >= 2:
			last_two = (queue[-2], queue[-1])
			if last_two in forms.keys():
				queue.pop()
				queue.pop()
				queue.append(forms[last_two])
		
		for char in queue:
			clearers = [t[1] for t in opposed if t[0] == char]
		 	for clearer in clearers:
				if clearer in queue:
					queue = []
					
	return queue

runner()