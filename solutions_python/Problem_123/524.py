#!/usr/bin/python
import sys

maxT = 0
def getone(A, ns):
	global maxT
	#if maxT >=10:
	#	sys.exit(1)
	maxT += 1
	#print "Coming to A:", A
	#print ns
	res = 0
	if A == 1:
		return len(ns)
	
	if len(ns) == 0:
		#print "return 0"
		return 0
	if len(ns) == 1:
		if A <= ns[0]:
			#print "return 1"
			return 1
		#print "return 0"
		return 0

	if A <= ns[0]:
		#print "A smaller"
		# remove [0] 
		m1 = ns[1:]
		res1 = 1 + getone(A, m1)
		m2 = ns[:]
		A = A+A-1
		res2 = 1 + getone(A, m2)
		if res1 <= res2:
			#print "return ", res1
			return res1
		else:
			#print "return ", res2
			return res2
	else:
		# A > ns[0]
		#print "A biger"
		A = A + ns[0]
		ns = ns[1:]
		res = getone(A, ns)
		return res

def treatone(j, A, N, nss):
	res = 0
	ns = []
	for strn in nss:
		ns.append(int(strn))

	ns.sort()
	#print "Case #%d, A=%d, N=%d, "%(j, A, N)
	
	res = getone(A, ns);
	print "Case #%d: %d"%(j, res)
	#print ""

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
		A = int(arr[0])
		N=int(arr[1])
		line=f.readline()
		ns = line.split()
		treatone(j , A, N, ns);
	
if __name__ == "__main__":
	testmain()
