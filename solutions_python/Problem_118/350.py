#fi=open("C-small-attempt0.in",'r')#Input File
#fo=open("C-small-attempt0.in",'w')#Output File

fi=open("C-large-1.in",'r')#Input File
fo=open("C-large-1.out","w")#Output File

#fi=open("C.in",'r')#Input File
#fo=open("C.out","w")#Output File

import math

def is_palindrom(n):
    x = str(n)
    y = x[::-1]
    return x == y
    
lst = []
a = 1
b = 100000000000000
a = int(math.ceil(math.sqrt(a)))
b = int(math.floor(math.sqrt(b)))
for i in range(a, b+1):
    sq = i**2
    if is_palindrom(i) and is_palindrom(sq):
        lst.append(sq)

T=int(fi.readline())
for case in range(1,T+1,1):
	ans=0
	############################################
	a, b = map(int, fi.readline().split())
	for i in lst:
	    if i >= a and i <= b:
	        ans += 1
	        
	############################################
	fo.write("Case #%s: %s\n"%(case, ans))
