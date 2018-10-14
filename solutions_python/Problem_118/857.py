import sys
import math

def getp(i):
	return str(i)+str(i)[::-1]

def getp2(i):
	return str(i)+str(i)[-2::-1]

def isp(s):
	l=len(s)
	for i in xrange(0,l/2+1):
		if s[i]!=s[l-i-1]:
			return 0
	return 1

T = int(sys.stdin.readline().strip())
for t in xrange(T):
	line=sys.stdin.readline().strip().split(' ')
	a=int(line[0])
	b=int(line[1])
	count=0
	i=1
	mx=a
	while i<mx:
		x=int(i+mx)/2
		y=int(getp(x))
		if y*y>a:
			mx=x
		else:
			i=x+1
	i=max(i-1,1)
	while 1:
		x=getp(i)
		y=int(x)
		y*=y
		if y>=a and y<=b and isp(x) and isp(str(y)):
			count+=1
			#print x,y
		x=getp2(i)
		y=int(x)
		y*=y
		if y>b:
			break
		if y>=a and isp(x) and isp(str(y)):
			count+=1
			#print x,y
		i+=1
	print 'Case #%d:' % (t+1), count
