f = open("a.in")
d = f.read()
f.close()

d = d.split("\n")

t = int(d[0])

def simu(l):
	tm = 0
	po = 1
	pb = 1
	
	tO = 0
	tB = 0
	
	ltO = 0
	ltB = 0
	
	lastTime = 1
	
	for i in xrange(len(l)/2):
		rob = l[i*2]
		pos = int(l[i*2+1])
		
		#print "1) ", rob, pos, po, pb, tm
		
		if rob == "O":
			_ltO = 1
			if abs(pos - po) > ltB:
				_ltO += abs(pos - po) - ltB
			ltO += _ltO
			ltB = 0
			tm += _ltO
			po = pos
			
		else:
			_ltB = 1
			if abs(pos - pb) > ltO:
				_ltB += abs(pos - pb) - ltO
			ltB += _ltB
			ltO = 0
			tm += _ltB
			pb = pos
		
		#print "2) ", rob, pos, po, pb, tm
	
	return tm

f = open("a.out", "w")
for ti in xrange(t):
	l = d[ti+1].split(" ")[1:]
	S = "Case #%d: %d" % ((ti+1), simu(l))
	print S
	f.write("%s\n" % S)
f.close()

