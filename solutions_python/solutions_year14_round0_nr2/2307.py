import sys
fpin=open('B-large.in','r')
fpout=open('outa.txt','w')
sys.stdin=fpin
sys.stdout=fpout
T=input()
for testcase in xrange(1,T+1):
	C,F,X=map(float,raw_input().split(' '))
	lasttime=X/2.0
	cnt=0
	totaltime=C/(2+cnt*F)
	while totaltime+X/(2+(cnt+1)*F)<lasttime:
		lasttime=totaltime+X/(2+(cnt+1)*F)
		cnt+=1
		totaltime+=C/(2+cnt*F)
	print 'Case #%d:'%(testcase),lasttime
fpin.close()
fpout.close()