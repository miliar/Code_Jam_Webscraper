#usr/bin/python
from __future__ import division
import sys

fin = open(sys.argv[1], "r")
fout = open("B.out", "w")
     

T = int(fin.readline())
for ii in xrange(T):
	num_in = list(fin.readline().rstrip())
	print (num_in)
	if len(num_in) > 1:
		for i in range(len(num_in)-1):
			if int(num_in[i]) > int(num_in[i+1]):
				num = int(num_in[i])
				num_in[i] = str(int(num_in[i]) - 1)
				for j in range(i+1, len(num_in)):
					num_in[j] = '9'
				if i > 0:
					for j in range(1,i+1):
						print (num_in[i-j], num_in[i-j+1])
						if int(num_in[i-j]) == num:
							num_in[i-j+1] = '9'
							num_in[i-j] = str(num - 1)
				break
	for i in range(len(num_in)):
		if num_in[0] == '0':
			num_in = num_in[1:]
	out = ''.join(num_in)





	fout.write("Case #" + str(ii+1) + ": " + str(out) + "\n")