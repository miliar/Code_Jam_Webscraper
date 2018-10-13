from __future__ import division, with_statement
from itertools import *
from numpy import *
from collections import *

def main():
	#~ lines = file("A-example.in").readlines()
	#~ lines = file("A-small.in").readlines()
	lines = file("A-large.in").readlines()
	lines.reverse()
	output = []
	num_tests = int(lines.pop())
	for test in xrange(1, num_tests+1):
		#~ print "test", test
		N, K = map(int, lines.pop().split())
		#~ print N, K

		if 0:

			snapper_power = zeros(N+1, dtype=bool)
			snapper_power[0] = 1
			snapper_power[1] = 1
			snapper_on = zeros(N+1, dtype=bool)
			snapper_on[0] = 1

			on_state = 1

			#~ print -1, snapper_power, snapper_on
			for k in xrange(K):

				# toggle
				for n in range(1,N+1):
					if snapper_power[n]:
						snapper_on[n] = not snapper_on[n]
						#~ print n, snapper_on

				# set powered
				for n in range(1,N+1):
					snapper_power[n] = snapper_power[n-1] * snapper_on[n-1]

				#~ print k, snapper_power.astype(int), snapper_on.astype(int)
				#~ on_state
				on_state = int("".join(map(str, reversed(snapper_on.astype(int)))), 2)
				#~ print on_state

			#~ print K, on_state, (K*2+1) % (2**(N+1))
			#~ print on_state, ((K-1)*2+1) % (2**(N+1))
			#~ print (on_state+1) // (2**(N+1)) == 1
			state = snapper_power[-1] and snapper_on[-1]

		on_state = (K*2+1) % (2**(N+1))
		state = ((on_state+1) // (2**(N+1)) == 1)
		#~ print state
		output.append("Case #%d: %s" % (test, "ON" if state else "OFF"))
		#~ print

	#~ with file("A-example-out.txt", "w") as f:
	#~ with file("A-small-out.txt", "w") as f:
	with file("A-large-out.txt", "w") as f:
		s = "\n".join(output)
		f.write(s)
		print s

if __name__ == "__main__":
	#~ main_a()
	main()
