#!/usr/bin/python
import sys
def gcd(a,b):
	while b>0:
		a,b=b,a%b
	return a

t=int(sys.stdin.readline())
order=0
while t>0:
	t=t-1
	order=order+1
	line=sys.stdin.readline().strip().split()
#print line
	n=len(line)-1
	if n != int(line[0]):
		print "Read error"
	line=line[1:]
	num=[]
	for i in range(len(line)):
		num.append(int(line[i]))
	num.sort()
	g=num[n-1]-num[0]	
	if g==0:
		print "Infinit"
		continue
	for i in range(n-1):
		g=gcd(g,num[i+1]-num[i])
	ans=g-(num[0]%g)
	if ans==g: ans=0
	print "Case #%d: %d" % (order,ans)
		
