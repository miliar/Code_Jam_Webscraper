from operator import itemgetter, attrgetter
import os, logging

FILE = 'A-large'

if __name__ == "__main__":
	import doctest, Bot_trust
	doctest.testmod(Bot_trust)


def runner():
	path = os.path.join(os.path.dirname(__file__), 'input', '%s.in.txt' % FILE)
	f = open(path, 'r')
	
	path = os.path.join(os.path.dirname(__file__), 'output', '%s.out.txt' % FILE)
	r = open(path, 'w')
	
	for n, test_case in enumerate(f.readlines()[1:]):
		r.write('Case #%r: %r\n' % (n+1, robot(test_case)))
	
	f.close()
	r.close()
	
	
def robot(test_case):
	'''
	>>> robot('4 O 2 B 1 B 2 O 4')
	6

	>>> robot('3 O 5 O 8 B 100')
	100

	>>> robot('2 B 2 B 1')
	4
	
	'''
	
	l = test_case.split()
	given_cases = int(l[0])
	l = l[1:]
	
	instructions = []
	for i in xrange(0, given_cases):
		instructions.append((l[i*2], int(l[i*2+1])))
		
	logging.warning(instructions)
	
	B_loc = 1
	O_loc = 1
	
	instructions.reverse()
	B_destinations = [instrux[1] for instrux in instructions if instrux[0] == 'B']
	O_destinations = [instrux[1] for instrux in instructions if instrux[0] == 'O']
	pressers = [instrux[0] for instrux in instructions]

	def next(l):
		if l:
			return l.pop()
		else:
			return 0

	presser = next(pressers)
	B_dest = next(B_destinations)
	O_dest = next(O_destinations)
	
	turns = 0
			
	while True != False:
		turns += 1
		B_skip = False
		O_skip = False
		
		if presser == 'B' and B_loc == B_dest:
			presser = next(pressers)
			B_dest = next(B_destinations)
			B_skip = True
		elif presser == 'O' and O_loc == O_dest:
			presser = next(pressers)
			O_dest = next(O_destinations)
			O_skip = True
		
		if not B_skip: B_loc += max(-1,min(1, (B_dest - B_loc)))
		if not O_skip: O_loc += max(-1,min(1, (O_dest - O_loc)))
		
		if not presser: break

	return turns
	
runner()