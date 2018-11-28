import sys
import re


if __name__=="__main__":
	fp = sys.stdin
	s  = fp.readline()
	times = int(s)
	for loop in range(0 , times):
		print "Case #%d:" % (loop+1),
		s = fp.readline()
		ss = re.findall('\d+' , s)
		n = int(ss[0])
		k = int(ss[1])

		res = True
		if (k == 0):
			res = False
		else:
			t = 2**n
			if (k + 1) % t == 0:
				res = True
			else:
				res = False

		if res:
			print "ON"
		else:
			print "OFF"
