import sys
import math


def log2_int(x):
	return x.bit_length() - 1


# print log2_int(8)



T = int(raw_input())

for i in xrange(1, T + 1):
	N, K = [int(x) for x in raw_input().split(" ")]
	
	n = N

	#you have to cut log2_int(K) + 1 times to get to the right level, log2_int(K) times to get to the parent

	logvalue = log2_int(K)
	# print logvalue
	k = K - (2**logvalue)
	# print k

	#use binary representation of k to get sequence of left and right branches

	for j in xrange(0, logvalue):
		# print 'start n: ' + str(n)
		if((k >> j) & 1 == 0):
			n = n - 1 - ((n - 1) // 2)
			# print 'end n ' + str(n)
		else:
			n = (n - 1) // 2
			# print 'end n ' + str(n)

	#at this point n is the parent of the outputs

	result = "Case #" + str(i) + ": "
	result += str(n - 1 - ((n - 1) // 2)) + " " + str((n - 1) // 2)
	print result

