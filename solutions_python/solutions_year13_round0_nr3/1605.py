import sys
import time
import math

with open(sys.argv[1]) as f:
	T  = int(f.readline())
	content = f.readlines()



palins = {}
sqrs = {}

def solve(a,b):
	#print 'Lets solve %d : %d' % (a,b)
	cnt = 0
	for sqr in sqrs:
		#print 'Lets try %d' % sqr
		pal = int(sqr ** 0.5)
		if int(pal**2) != sqr:
			continue
		sqrstr = str(sqr)
		#print sqrstr, sqrstr[int((len(sqrstr)+1)/2)::-1],int((len(sqrstr)+1)/2)
		sqrstr = sqrstr[:int((len(sqrstr))/2)]+sqrstr[:int((len(sqrstr)+1)/2)][::-1]
		#print sqrstr, sqr,int((len(str(sqr))+1)/2),len(str(sqr))
		
		if sqrstr != str(sqr):
			continue

		#print 'created %s from %d' % (sqrstr,  sqr)
		#if palins[sqr] and pal >=a and pal <= b:
		if palins[pal] and sqr >=a and sqr <= b:
			cnt = cnt + 1
			#print 'Found fair and square! %d %d' % (pal,sqr)
	return cnt
def ispalin(v):
	v = str(int(v))
	vv = v[:int((len(v))/2)]+v[:int((len(v)+1)/2)][::-1]
	return vv == v

def fair(max):
	length = int(math.log10(max)+1)
	rounds = int(length / 2)
	extra = length & 1
	for k in range(10):
		palins[k] = True
		sqrs[k**2] = True
	for digits in range(1,rounds+1,1):
		#print 'Preprocessing %d of %d' % (digits, rounds)
		#print 'Generate length %d' % digits
		for val in range(10**(digits-1),10**(digits),1):
			palin = int(str(val) + str(val)[::-1])
			if(ispalin(palin**2)):
				palins[palin] = True
				sqrs[palin**2] = True
			#print 'Created palindrome %s from %s' % (palin,val)
			if extra == 1 or rounds < digits:
				for mid in range(0,10):
					palin = int(str(val) + str(mid) + str(val)[::-1])
					if(ispalin(palin**2)):
						palins[palin] = True
						sqrs[palin**2] = True
					#print 'Created palindrome %s from %s' % (palin,val)

def preprocess(max):
	fair(max)


preprocess(10**14)

for t in range(T):
	args = content[t].split()
	a = int(args[0])
	b = int(args[1])
	print 'Case #%d: %s' % (t+1,solve(a,b))