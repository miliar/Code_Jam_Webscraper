from sys import stdin

def baseconvert(number,fromBase):
	c = 0	
	r = 0
	for i in xrange(len(str(number))-1,-1,-1):
		r += int(str(number)[i]) * (fromBase**c)
		c += 1
	return r

fil = open("out1.out","w")

T = int(stdin.readline().strip())
for i in xrange(0,T):
	line = stdin.readline().strip()
	nbrs = {}
	cntr = 0	
	for char in line:
		if not char in nbrs.keys():
			if cntr == 0:
				nbrs[char] = 1
			else:
				if cntr == 1:
					nbrs[char] = 0
				else:					
					nbrs[char] = cntr
			cntr += 1
	m = 0
	s = ""
	for char in line:
		s += str(nbrs[char])
	for val in nbrs.values():
		m = val if val > m else m
	v = baseconvert(int(s),m+1)
	finalstr = "Case #" + str((i+1)) + ": " + str(v)	
	fil.write(finalstr + "\n")
fil.close()
