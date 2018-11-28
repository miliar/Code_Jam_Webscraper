from __future__ import print_function
import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		log('processing case %d' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	x, r, c = map(int, sys.stdin.readline().split())

	won = True
	angled_pair = (x / 2 if x % 2 == 0 else x / 2 + 1, x / 2 + 1)

	if x >= 7:
		log('..wonky enclave')
		won = False

	elif r * c % x != 0:
		log('..doesn\'t fit')
		won = False

	elif x <= 2:
		pass

	elif x > r and x > c:
		log('..got blocked out')
		won = False

	elif min(r, c) < x - 1:
		won = False

	# elif min(r, c) <= angled_pair[0] or max(r, c) <= angled_pair[1]:
	# 	log('..got blocked out')
	# 	won = False

	# elif min(r, c) == angled_pair[0] or max(r, c) == angled_pair[1]:
	# 	log('..wonky island')
	# 	won = False

	sys.stdout.write('Case #%d: %s\n' % (case, 'GABRIEL' if won else 'RICHARD'))

def log(msg):
	sys.stderr.write('%s\n' % msg)

if __name__ == '__main__':
	main()
