import sys
import math

def main():
	t = int(sys.stdin.readline())
	for case in range(1, t+1):
		sys.stderr.write('processing case %d\n' % case)
		process_case(case)
	sys.stderr.write('Finished!\n')

def process_case(case):
	c, f, x = map(float, sys.stdin.readline().split())
	n = 0
	time = get_time(c, f, x, n)
	while True:
		n = n + 1
		next_time = get_time(c, f, x, n)
		if next_time > time:
			sys.stdout.write('Case #%d: %s\n' % (case, str(time)))
			return
		else:
			time = next_time

def get_time(c, f, x, n):
	time = 0.0
	rate = 2.0
	for i in range(n):
		rate = 2.0 + (float(i) * f)
		time = time + (c / rate)
	rate = 2.0 + (float(n) * f)
	time = time + (x / rate)
	return time

if __name__ == '__main__':
	main()
