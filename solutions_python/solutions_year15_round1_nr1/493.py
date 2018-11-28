from __future__ import division
import sys,copy
from  itertools import combinations,permutations
from bisect import bisect_left
# print list(combinations(array,i))
sys.stdin=open('A-large.in','r')
sys.stdout=open('ans','w')
# print "Case #"+str(num+1+": "+str(ans)
def all_p(s):#s is string
	return list(map("".join,permutations(s)))
def pow_mod(x, y, z):# a^b%c
    "Calculate (x ** y) % z efficiently."
    number = 1
    while y:
        if y & 1:
            number = number * x % z
        y >>= 1
        x = x * x % z
    return number
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end
def r1():
	return raw_input().split()
def r():
	return map(int,raw_input().split())
def i():
	return input()
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


for num in range(input()):
	n = input()
	arr= r() 
	# case 1
	ans1=0
	for i in range(1,n):
		if arr[i]>=arr[i-1]:continue
		else:
			ans1+=abs(arr[i]-arr[i-1])
	# case 2
	m=0
	ans=0
	for i in range(1,n):
		if arr[i]<=arr[i-1]:
			m=max(m,(arr[i-1]-arr[i])/10)
	if m==0:
		ans=0
	else:
		# print m
		for i in range(n-1):
			# print arr[i],10/m,
			ans+=min(arr[i],10*m)
		# print ans
	ans,ans1=int(ans),int(ans1)
	print "Case #"+str(num+1)+": "+str(ans1)+" "+str(ans)


	# print ans1,ans



	
