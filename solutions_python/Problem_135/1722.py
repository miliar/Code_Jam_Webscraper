import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		sys.stderr.write('processing case %d\n' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	first_row = int(sys.stdin.readline().strip()) - 1
	first_grid = [map(int, sys.stdin.readline().split()) for i in range(4)]
	second_row = int(sys.stdin.readline().strip()) - 1
	second_grid = [map(int, sys.stdin.readline().split()) for i in range(4)]
	possible = list(set(first_grid[first_row]).intersection(set(second_grid[second_row])))
	if len(possible) == 1:
		sys.stdout.write('Case #%d: %d\n' % (case, possible[0]))
	elif len(possible) > 0:
		sys.stdout.write('Case #%d: %s\n' % (case, 'Bad magician!'))
	else:
		sys.stdout.write('Case #%d: %s\n' % (case, 'Volunteer cheated!'))

if __name__ == '__main__':
	main()
