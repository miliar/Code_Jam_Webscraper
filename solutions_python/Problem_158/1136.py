# your code goes here
def rules(x,r,c):
	if x == 1:
		return 'GABRIEL'
	elif x>6:
		return 'RICHARD'
	elif (r*c)%x != 0:
		return 'RICHARD'
	elif (r<x and c<x):
		return 'RICHARD'
	elif r%x == 0:
		if c<x-1:
			return 'RICHARD'
	elif c%x == 0:
		if r<x-1:
			return 'RICHARD'
	return 'GABRIEL'
	
T = input()
for i in range(T):
	x, r, c = raw_input().split()
	x = int(x)
	r = int(r)
	c = int(c)
	ans = rules(x, r, c)
	print("Case #" + str(i+1) + ": " + ans)
	
	
	
	
