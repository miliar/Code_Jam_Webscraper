def p(str):
	#print str
	pass

def nextNum(n):
	l = []
	for n2 in n:
		l.append(int(n2))
	l.sort()
	#print l
	
	i = int(n)+1

	while True:
		p( ">> n:%d, a:%d"  % (int(n),i))
		if isMatch(l,i): return i
		i += 1

def isMatch(l,num):
	lc = l[:]
	# check input num matches array
	i = 1
	while True:
		n = num % 10
		p(n)
		p(lc)
		if n not in lc: 
			if n != 0:
				return False
		else:
			lc.remove(n)
		if num < 10: break
		num /= 10
	p("exits:")
	p(lc)
	if len(lc) > 0: return False
	return True

p(nextNum("6233"))
#p(isMatch([1,1,5],115))
