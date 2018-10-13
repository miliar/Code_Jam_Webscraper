import math
def reverse(num):
	return int(str(num)[::-1])
n=input()
d=1
while n>0:
	a,b=raw_input().split()
	a=int(a)
	b=int(b)
       # a=int(round(math.sqrt(a)+.5));
       # b=int(round(math.sqrt(b)-.5));
        count=0
        for i in xrange(a,b+1):
  	     sqr=math.sqrt(i)
             if i==reverse(i) and sqr==int(sqr) and int(sqr)==reverse(int(sqr)):
             	count=count+1
        print "Case #%d: %d"%(d,count)    
        n=n-1
        d=d+1
