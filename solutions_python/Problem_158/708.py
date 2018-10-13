tests = int(raw_input())
for i in range(tests):
	x,r,c = raw_input().split(" ")
	x = int(x)
	r = int(r)
	c = int(c)
	board = c*r
	if x == 4 and board == 8:
		print 'Case #{}: RICHARD'.format(i+1)
	elif (c==1 or r==1) and x>2:
		print 'Case #{}: RICHARD'.format(i+1)
	elif x == 1:
		print 'Case #{}: GABRIEL'.format(i+1)
	elif (x==c==2 and r ==1) or (x==r==2 and c==1):
		print 'Case #{}: GABRIEL'.format(i+1)
	elif (x==c and r == 1) or (x==r and r==1):
		print 'Case #{}: RICHARD'.format(i+1)
	elif board%x!=0 or (x > c and x > r):
		print 'Case #{}: RICHARD'.format(i+1)
	else:
		print 'Case #{}: GABRIEL'.format(i+1)