def fun():
	inp = [int(x) for x in raw_input().split()]
	N = inp[0]
	pocz = inp[1]
	kon = inp[2]
	inp = [int(x) for x in raw_input().split()]
	found = False
	
	for i in range(pocz,kon+1):
		cnt = 0
		for k in inp:
			if(i%k==0 or k%i ==0):
				cnt+=1;
		if(cnt==len(inp)):
			return str(i)
	return "NO"

tests = int(raw_input())
t = 1
while(t<=tests):
	print "Case #%s: %s"%(t,fun())
	t+=1
	


#sortowanie
#from operator import itemgetter
#sorted(arr,key=itemgetter(2))

#import operator
#s = sum(map(operator.mul,arr1,arr2))
#r = reduce(operator.xor,a)
	
