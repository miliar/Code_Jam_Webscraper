def solve(X,R,C):
	if R > C:
	    tmp = C
	    C = R
	    R = tmp
	if R * C % X != 0:
	    return False
	if X < 3:
	    return True
	ans = False
	ans |= (X == 3) and (R == 2) and (C == 3)
	ans |= (X == 3) and (R == 3) and (C == 3)
	ans |= (X == 3) and (R == 3) and (C == 4)
	ans |= (X == 4) and (R == 3) and (C == 4)
	ans |= (X == 4) and (R == 4) and (C == 4)
	return ans

def result(X,R,C):
	if solve(X,R,C):
		return "GABRIEL"
	else:
		return "RICHARD"

t = input()
case = 1
while t:
	t -= 1
	X,R,C = map(int,raw_input().split())
	print "Case #%d: %s" % (case, result(X,R,C))
	case += 1