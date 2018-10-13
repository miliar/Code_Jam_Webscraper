t = int(raw_input())

def str_fixed(sz, n):
	s = str(n)
	while (len(s) < sz):
		s = "0" + s 
	return s


for c in range(t):
	n = int(raw_input())

	sz = len(str(n))

	pow_10 = 1

	for i in range(sz-1, 0, -1):
		#print i
		str_n = str_fixed(sz,n)
		if (int(str_n[i]) >= int(str_n[i-1]) ):
			#todo piola
			pass
		else:
			#print n, i, int(str_n[i]) + 1
			n -= (int(str_n[i:sz]) + 1)

		pow_10 *= 10 

	print "Case #{0}: {1}".format(c+1, n) 



