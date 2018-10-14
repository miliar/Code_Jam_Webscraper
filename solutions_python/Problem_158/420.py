T = int(raw_input())

def solve(x,r,c):
	
	if r < c: r,c=c,r
	
	if x == 1: return True
	
	elif x == 2:
		if r<2 or c<1: return False
		elif r*c % 2 == 0: return True
		else: return False
		
	elif x == 3:
		if r < 3 or c < 2: return False
		elif r*c % 3 == 0: return True
		else: return False
		
	elif x == 4:
		if r < 4 or c < 3: return False
		elif r*c % 4 == 0: return True
		else: return False
		
	

for i in range(T):
	X,R,C=(int(n) for n in raw_input().split())
	print "Case #%d: %s" % (i+1, "GABRIEL" if solve(X,R,C) else "RICHARD")
	
