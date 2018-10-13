import sys,os,math

a = 100
b = 114500
precalc_str = []
precalc_int = []

def readInput(filename):
	linia = 0
	coloana = 0

	f = open(filename)
	lines = f.readlines()

	nrTeste = int(lines[0])
	test = 1
	for line in lines[1:]:
		line = line.strip()
		a,b = line.split()
		#print "Testez:",a,b
		print "Case #%d:" % test,
		getCount(a,b)
		test += 1

	f.close()

def readPrecalculate(filename):
	global precalc_str, precalc_int
	f = open(filename)
	precalc = f.readlines()
	#print len(precalc)
	for i in precalc:
		precalc_int.append(int(i.strip()))


def isPalindrome(nr):
	orig = nr
	pal = 0	
	while nr > 0:
		r = nr % 10
		pal = pal*10 + r
		nr = nr / 10
	if orig == pal:
		return True
	return False

def getCount(a,b):
	global precalc_int
	count = 0

	a = float(a)
	sqrtA = int(math.sqrt(a))
	b = float(b)
	sqrtB = int(math.sqrt(b))
	for i in precalc_int:
		if ( i >= sqrtA ) and ( i<= sqrtB ):
			putere = i*i
			if putere < a:
				continue
			if putere > b:
				break
			if isPalindrome(putere):
				count += 1

#	a = int(a)
#	b = int(b)
#	for i in xrange(a, b+1):
#		if isPalindrome(i):
#			q = int(math.sqrt(i))
#			#print i,q,q*q
#			if isPalindrome(q):
#				if q*q == i:
#					print i
#					count += 1

	print count


readPrecalculate("all_palindr2.txt")
readInput("C-large-1.in")
