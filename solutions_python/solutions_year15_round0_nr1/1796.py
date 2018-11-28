from __future__ import print_function
import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		sys.stderr.write('processing case %d\n' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	params = sys.stdin.readline().split()
	s_max = int(params[0])
	audience = [int(ch) for ch in params[1]]
	needed = 0
	total = 0
	for i in range(1, s_max + 1):
		total += audience[i-1]
		needed += max((i - (total + needed)), 0)

	sys.stdout.write('Case #%d: %d\n' % (case, needed))

if __name__ == '__main__':
	main()
