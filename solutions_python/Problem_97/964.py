def recy(s):
	for ix in range(len(s)):
		if (s[ix] != '0'):
			yield s[ix:]+s[:ix]

def solve():
	fi = open('recycled_small_in.txt','r')
	fo = open('recycled_small_out.txt','w')
	T = int(fi.readline())
	for t in xrange(1,T+1):
		a,b = map(int,fi.readline().strip().split())
		
		gc = {}
		for i in range(a,b+1):
			gm = None
			s = str(i)
			for rs in recy(s):
				if rs in gc.keys():
					gm = rs
			if gm != None:
				gc[gm] += 1
			else:
				gc[s] = 1
		
		res = 0
		for k in gc.keys():
			c = gc[k]
			if (c>=2):
				res += (c*(c-1))/2
		
		fo.write("Case #%d: %d\n"%(t,res))
	fi.close()
	fo.close()
