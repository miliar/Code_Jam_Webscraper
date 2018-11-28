"""
3n   : n,n,n     : n,n-1,n+1    (n,n+1)
3n+1 : n,n,n+1   : n-1,n+1,n+1  (n+1,n+1)
3n+2 : n,n+1,n+1 : n,n,n+2      (n+1,n+2)
"""

def func(n):
	if(n==1): return 1,0
	if(n==0): return 0,0
		
	if(n%3==0): return n/3,1
	if(n%3==1): return n/3+1,0
	if(n%3==2): return n/3+1,1
	

tc = int(raw_input())
for it in xrange(tc):
	test = map(int,raw_input().split(' '))
	surprises = test[1]
	trial = test[2]
	test = test[3:]
	good = 0
	ret = 0
	for i in test:
		ls = func(i)

		if(ls[0]>=trial):ret+=1
		elif(ls[0]+ls[1] >= trial) :good+=ls[1]
	ret+=min(good,surprises)
	print "Case #"+str(it+1) +":",ret
		
