import sys

if __name__ ==  "__main__":
        input = sys.stdin.readlines()
	c = 1;
        for line in input[1:]:
		v = line.split()
		v = map(int,v)
		n = v[0]
		s = v[1]
		p = v[2]
		if p == 0:
			print "Case #%d: %d" % (c,n)
			c = c + 1
			continue
		t = v[3:]
		t.sort()
		out = 0;
		for ti in t:
			if p == 1:
				if ti > 0:
					out = out + 1
			else:
				if ti > (p-1)*3:
					out = out + 1
				elif s>0 and ( ti == (p-1)*3 or ti == (p-1)*3-1):
					out = out + 1
					s = s - 1
		print "Case #%d: %d" % (c,out)
		c = c + 1
