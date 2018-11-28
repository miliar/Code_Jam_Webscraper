import copy
import math

T = int(raw_input().strip())

for i in range(T):
	Nt,Kt = (raw_input().strip()).split(' ')
	N = int(Nt)
	K = int(Kt)
	if(((K+1) % (1<<N)) == 0):
		s = 'Case #' + repr(i+1) + ': ON'
		print s
	else:
		s = 'Case #' + repr(i+1) + ': OFF'
		print s
