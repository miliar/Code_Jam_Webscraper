#!/usr/bin/python
import sys
pie = 3.141592659

def treatone(j, r, t):
	#print "Case #%d: %s"%(j, resP[res])
	#print "r=%d, t=%d"%(r, t)
	#count = t/pie
	a = 4
	b = 4*r +6
	c = 4*r +2 -2*t
	
	delta = b * b -4*a*c +0.0
	
	delta = pow(delta, 0.5)

	k = int((0-b + delta)/(2.0*a))
	check = 4 * k * k + (4 * r + 6)*k + (4*r + 2 - 2*t)
	#print check
	if check > 0:
		res = k
	else:
		res = k +1
	print "Case #%d: %s"%(j, res)
	

def testmain():
	if(len(sys.argv)<2):
		return

	fname = sys.argv[1]
	f = open(fname)
	line=f.readline()
	Ts = int(line.strip())
	
	#print Ts
	j=0
	part = []
	while True:
		j += 1
		if(j>Ts):
			return
		line=f.readline()
		#print "read " ,line
		if(len(line)<=0):
			#print "line less"
			break
		line = line.strip()
		arr = line.split()
		r = int(arr[0])
		t=int(arr[1])
		treatone(j , r, t);
	
if __name__ == "__main__":
	testmain()
