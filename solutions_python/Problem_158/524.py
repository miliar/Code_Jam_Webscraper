import sys

t = int(input())
k = 1
while t>0:
	t -= 1
	sys.stdout.write('Case #'+str(k)+': ')
	k += 1
	x, r, c = [int(a) for a in raw_input().split()]
	r, c = min(r, c), max(r, c)
	if x>r and x>c:
		print 'RICHARD'
	elif (r*c)%x != 0:
		print 'RICHARD'
	elif x<=r and x<=c:
		print 'GABRIEL'
	else:
#		print 'Hello', x, r, c 
		if x==3 and r==1 and c==3:
			print 'RICHARD'
		elif x==4 and r<=2:
			print 'RICHARD'
		else:
			print 'GABRIEL'
	pass