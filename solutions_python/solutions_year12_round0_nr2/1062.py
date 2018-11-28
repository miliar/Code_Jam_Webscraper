def	readint():
	return	(list(map(int,	sys.stdin.readline().strip().split(" "))))
def	readstr():
	return	(list(map(str,	sys.stdin.readline().strip().split("	"))))
def	rline():
	return	sys.stdin.readline().strip()


import	sys
testcase	=	int(rline())
for	i	in	range(testcase):
	l	=	readint()
	n = l[0]
	s = l[1]
	p = l[2]
	minp = 3*p -2
	if minp < p:
		minp = p
	count = 0
	#print (n, s, p)
	for score in  l[3:]:
		#print (score, minp)
		if score >= minp:
			count += 1
		elif s > 0 and score >= abs(3*p-4):# and score >= p:
			#print (score,  abs(3*p-4), s)
			s -=1
			count +=1
	print	('Case	#%d: %d' % ((i+1),count))