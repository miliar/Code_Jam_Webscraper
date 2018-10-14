#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("A.out", "w")
     

T = int(fin.readline())
for ii in xrange(T):
	sign_array, k = fin.readline().split(' ')
	k = int(k)
	sign_array = list(sign_array)
	print (sign_array, k)
	out = 0
	for i in range(len(sign_array)):
		if sign_array[i] == '-' and (len(sign_array)-i)>=k:
			for j in range(i, i+k):
				if sign_array[j] == '-':
					sign_array[j] = '+'
				else:
					sign_array[j] = '-'
			out = out + 1
		elif sign_array[i] == '-':
			for j in range(i, len(sign_array)):
				if sign_array[j] == '-':
					out = 'IMPOSSIBLE' 




	fout.write("Case #" + str(ii+1) + ": " + str(out) + "\n")
