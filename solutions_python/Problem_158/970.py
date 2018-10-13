f=open('D-small-attempt4.in','r')
g=open('D.out','w')
inp=[]
for line in f:
	inp.append(line)
for i in range(1,65):
	x,r,c=map(int,inp[i].split())
	if x==1:
		g.write('Case #'+str(i)+': GABRIEL\n')
	if x==2 and (r*c)%2==0:
		g.write('Case #'+str(i)+': GABRIEL\n')
	if x==2 and (r*c)%2==1:
		g.write('Case #'+str(i)+': RICHARD\n')
	if x==3:
		if r*c==9 or r*c==6 or r*c==12:
			g.write('Case #'+str(i)+': GABRIEL\n')
		else:
			g.write('Case #'+str(i)+': RICHARD\n')
	if x==4:
		if r*c==12 or r*c==16:
			g.write('Case #'+str(i)+': GABRIEL\n')
		else:
			g.write('Case #'+str(i)+': RICHARD\n')

