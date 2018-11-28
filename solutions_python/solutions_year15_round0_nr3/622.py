#Google Code Jam 2015 
#Problem C. Dijkstra
#Author: vectorijk

def solve(L,X,s):
	found = False
	ans = '1'
	neg = False
	foundI = False
	foundJ = False
	for i in range(0,X):
		ret = Eval(s,ans,neg,foundI,foundJ)
		ans,neg,foundI,foundJ = ret
	if neg and ans == '1' and foundI and foundJ:
	    found = True
	if found:
	    return "YES"
	else:
	    return "NO"

def Eval(s, ans, neg, fI, fJ):
	for i in s:
		neg = neg ^ sign(ans, i)
		ans = mult(ans, i)
		if ans == 'i' and neg == False:
			fI = True
		if fI == True and ans == 'k' and neg == False:
			fJ = True
	return (ans,neg, fI, fJ)

def mult(a, b):
	if a == '1':
	    return b
	if b == '1':
	    return a
	if a == b:
	    return '1'
	if a == 'i':
		if b == 'j':
		    return 'k'
		if b == 'k':
		    return 'j'
	if a == 'j':
		if b == 'i':
		    return 'k'
		if b == 'k':
		    return 'i'
	if a == 'k':
		if b == 'i':
		    return 'j'
		if b == 'j':
		    return 'i'
	return '0'

def sign(a, b):
	if a == '1' or b == '1':
	    return False;
	if a == b:
	    return True;
	if (a == 'i' and b == 'k' or a == 'j'  
		and b == 'i' or a == 'k'
		and b == 'j'):
	    return True
	return False

t = input()
case = 1
while t:
	t -= 1
	L,X = map(int,raw_input().split())
	s = raw_input()
	print "Case #%d: %s" % (case, solve(L,X,s))
	case += 1