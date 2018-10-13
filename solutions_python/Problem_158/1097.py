T = input()
for _ in range(0,T):
	inp = raw_input().split(' ')
	X,R,C = int(inp[0]),int(inp[1]),int(inp[2])
	ret = ''
	if X == 1:
		ret = 'GABRIEL'
	if X == 2:
		if R*C%2==0:
			ret = 'GABRIEL'
		else:
			ret = 'RICHARD'
	if X == 3:
		if R*C%3==0 and min(R,C)>1:
			ret = 'GABRIEL'
		else:
			ret = 'RICHARD'
	if X==4:
		if R*C==16 or R*C==12:
			ret = 'GABRIEL'
		else:
			ret = 'RICHARD'
	print "Case #" + str(_+1) + ": " + str(ret)

