# by shik
import sys
sys.stdin=open("B-large.in")
sys.stdout=open("B-large.out","w")
def gcd(a,b):
	if b==0 : return a
	else : return gcd(b,a%b)
def abs(x):
	if x<0 : return -x
	else : return x
# main
c=int(input())
for t in range(1,c+1):
	arr=input().split()
	n=int(arr[0])
	for i in range(1,n+1) : arr[i]=int(arr[i])
	g=0
	for i in range(1,n) : g=gcd(g,abs(arr[i+1]-arr[i]))
	print("Case #%d: %d"%(t,(g-arr[1]%g)%g))