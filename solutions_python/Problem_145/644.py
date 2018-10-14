import math
def gcd(a, b):
        if (b == 0):
		return a
	else :
		return gcd(b, a % b)

def solve(f, N):
	txt = f.readline()
	lst = txt.split('/')
	n = int(lst[0])
	d = int(lst[1])
	
	cd = gcd(n, d)
	n = n / cd
	d = d / cd

	lvlf = math.log(d, 2)
	lllf = math.log(n, 2)

	#print lvlf

	if (lvlf%1 != 0) :
		print "Case #"+str(N)+": impossible"
		return

	lvl = int(lvlf)
	lll = int(lllf)

	oo = lvl - lll

	#print lvl
	if (lvl > 40):
		print "Case #"+str(N)+": impossible"
	else:
		print "Case #"+str(N)+": "+str(oo)


def foo ():
	f = open('d://A-small-attempt1.in', 'r')
	num_cases = int(f.readline())
	for i in range (0, num_cases):
		solve(f, i+1)

foo()
