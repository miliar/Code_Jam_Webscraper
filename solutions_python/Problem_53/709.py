#!/usr/bin/python

f = open('A-large.in','r')
w = open('A-large.out','w')
testCases = int(f.readline())

for i in range(testCases):
	nk = [int(s) for s in f.readline().split(' ')]
	n = nk[0]
	k = nk[1]
	
	# A chain N snappers is represented by an N-bit binary number where the
	# first snapper is the LSB and the last snapper is the MSB.
	
	# A given snapper's state is represented by the value of the bit (0 is off 
	# and 1 is on).
	
	# Performing a snap causes the chainState to be incremented by 1
	# Thus, the least significant N bits of K represents the state of the chain.
	chainState = k % pow(2,n)
	
	# The light is ON iff the next snap will cause the entire chain to turn off
	lightState = 'OFF'
	if ( (chainState + 1) % pow(2,n) ) == 0:
		lightState = 'ON'
	
	w.write('Case #{0}: {1}\n'.format(i + 1, lightState))
