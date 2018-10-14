from math import *
def ispoli(v):
	a=[]
	while v>0:
		a.append(v%10)
		v/=10;
	for i in xrange(0,len(a)/2):
		if a[i]!=a[len(a)-i-1]:
			return False;
	return True;
	
def solve():
	(a,b)=map(int,raw_input().split())
	counter=0
	for i in xrange(a,b+1):
		root=sqrt(i)
		if int(root)!=root:
			continue;
		if ispoli(int(root)) and ispoli(i):
			#print i
			counter+=1
	return counter
def main():
	cn=int(raw_input())
	for cs in xrange(cn):
		print "Case #%d: %d" % (cs+1,solve())
if __name__=="__main__":
	main()
