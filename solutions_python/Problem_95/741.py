import math
inf = open("in.txt", "r")
ouf = open('out.txt','w')

def close_files():
	inf.close
	ouf.close

def precount():
	pass

printcounter = 0
def printstr(s):
	global printcounter
	printcounter +=1
	print >>ouf, 'Case #%d: %s' % (printcounter, s)
	#print >> ouf, st
	#print st

def add(a,b):
	return a + float(b)

def gcd(a,b):
	c = a
	d = b
	while c > 0:
		c, d = d %c, c
	return c+d

def solvetest():
	key = "yhesocvxduiglbkrztnwjpfmaq"
	a = inf.readline()
	out = ""
	for i in range(len(a)):
		if a[i] in key:
			out += key[ord(a[i])-ord("a")]
		elif a[i] == " ":
			out += " "
	#print out
	printstr(out)
		 
precount()
testnum = int(inf.readline())
for test in xrange(testnum):
	solvetest()
close_files()

