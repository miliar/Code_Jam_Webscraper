#AdiX
import math
testcase = int ( input() )

for itestcase in range(0,testcase):
	n,k = input().split(" ")
	n=int(n)
	k=int(k)
#	print(k+1)
#	print(2**(n+1))
#	print((k+1) % (2**(n)))
	c = int(2**n)-1
	if ((k <= n) and (k==c)):
		print("Case #"+str(itestcase+1)+": ON")	
	elif ((k+1) % (2**(n))) == 0 :
		print("Case #"+str(itestcase+1)+": ON")
	else:
		print("Case #"+str(itestcase+1)+": OFF")