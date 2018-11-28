C = int(raw_input())

def gcd(a,b):
	if a < b:
		a,b = b,a
	while b != 0:
		a,b = b,a%b
	return a

for i in range(C):
	test = map(lambda x:int(x),raw_input().split()[1:])
	res = abs(test[1]-test[0])
	for j in range(2,len(test)):
		res = gcd(res,abs(test[j]-test[0]))
	res = (1+(test[0]-1)/res)*res-test[0]
	print "Case #%d: %d"%(i+1, res)

