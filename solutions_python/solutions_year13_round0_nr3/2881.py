import math
def checkPal(num):
	digit=list(str(num))
	L=len(digit)
	l=int(L/2)
	for i in range(l):
		if digit[i]!=digit[L-i-1]: return False
	return True
	
T=int(raw_input())
for t in range(T):
	interval=raw_input().split()
	begin=int(interval[0])
	end=int(interval[1])
	sqrtBegin=math.ceil(math.sqrt(begin))
	sqrtEnd=math.floor(math.sqrt(end))
	#a=str(begin)+","
	count=0
	for i in range(int(sqrtBegin),int(sqrtEnd)+1):
		testSqr=i**2
		#a=a+str(testSqr)+","
		if checkPal(testSqr) and checkPal(i): 
			count=count+1
			
		
	#a=a+str(end)
	#print "{0}:{1}".format(a,count)
	#print "{0}:{1}".format(sqrtBegin,sqrtEnd)
	print "Case #{0}: {1}".format(t+1,count)
