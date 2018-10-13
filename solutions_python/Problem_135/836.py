
DEBUG=0
def l(n):
	#print 'n',n
	for i in range(4):
		la=f.readline().split(' ')
		la=[int(x) for x in la]
		#print int(n), i+1
		if(int(n)==i+1):
			l=la
	return l

BAD="Bad magician!"
CHEAT="Volunteer cheated!"


filename='A-small-0'
f=file('%s.in'%filename, 'r')
of=file('%s.out'%filename, 'w')
T=int(f.readline())
for t in range(T):
	n1=int(f.readline())
	l1=l(n1)
	n2=int(f.readline())
	l2=l(n2)
	
	ct=0
	answer=None
	for n in l2:
		if n in l1:
			ct+=1
			answer=str(n)
	if ct==0:
		answer=CHEAT
	if ct>1:
		answer=BAD
	of.write( "Case #%d: %s\n"%(t+1,answer))
