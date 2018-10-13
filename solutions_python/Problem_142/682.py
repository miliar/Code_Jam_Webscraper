'''
The Repeater
'''
def diff(l):
	return abs(l[0]-l[1])


if __name__ == '__main__':
	f=open("A-small-attempt0.in")
	nc=int(f.readline())
	for x in xrange(1,nc+1):
		# map(int, f.readline().strip().split(' '))
		ns = int(f.readline())
		ss = []
		for i in range(ns):
			ss.append(f.readline().strip())
		cadt = []
		cade = []
		for e in ss:
			o = list(e)
			p = o[0]
			pl = [p]
			plc = []
			c = 0
			for k in o:
				if k != p:
					pl.append(k)
					plc.append(c)
					c = 1
				else:
					c += 1
				p = k
			if len(plc) < len(pl):
				plc.append(c)
			#print plc
			cade.append(plc)
			cadt.append(pl)
		feglawon = False
		#print cadt
		for i in range(len(cadt)):
			if cadt[0] != cadt[i]:
				feglawon = True
		if feglawon:
			s = 'Fegla Won'
		else:
			v = sum(map(diff, zip(cade[0],cade[1])))
			s = str(v)
		print "Case #%d: %s" % (x, s)
