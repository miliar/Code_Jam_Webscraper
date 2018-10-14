T=int(raw_input())
for i in range(T):
	line=raw_input().split()
	x=int(line[0])
	r=int(line[1])
	c=int(line[2])
	m=min([r,c])
	if x==1:
		print 'Case #'+str(i+1)+': GABRIEL'
	elif x==2 and (r*c)%2==0:
		print 'Case #'+str(i+1)+': GABRIEL'
	elif x==3 and m>=2 and (r*c)%3==0:
		print 'Case #'+str(i+1)+': GABRIEL'
	elif x==4 and m>=3 and (r*c)%4==0:
		print 'Case #'+str(i+1)+': GABRIEL'
	else :
		print 'Case #'+str(i+1)+': RICHARD'
