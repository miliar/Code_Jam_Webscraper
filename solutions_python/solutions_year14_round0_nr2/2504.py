#!/usr/bin/env python
import sys

def main():
	# Setup input and output file handlers
	if len(sys.argv) == 1:
		f_in = sys.stdin
		f_out = sys.stdout
	else:
		f_in = open(sys.argv[1])
		if len(sys.argv) > 2:
			f_out = open(sys.argv[2], 'w')
		else:
			f_out = sys.stdout

	T = int(f_in.readline())
	for t in range(T):
		f_out.write('Case #%d: ' % (t+1))

		rate = 2.0 # Cookies per second
		C, F, X = list(map(float, f_in.readline().split(' ')))

		time_to_x = X/rate

		time_taken = C/rate
		rate += F

		while True:
			tmp = time_taken + X/rate
			if tmp > time_to_x:
				f_out.write('%.7f' % time_to_x)
				break
			time_to_x = tmp
			time_taken += C/rate
			rate += F

		f_out.write('\n')

	f_in.close()
	f_out.close()

if __name__=='__main__':
	main()
