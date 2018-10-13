import math

def isPalin(n):
	s = str(n)
	for i in range(0,int(len(s)/2)):
		if s[i] != s[-(i+1)]:
			return False
	return True
	
def isSqPalin(n):
	x = math.sqrt(n)
	if x != int(x):
		return False
	return isPalin(int(x))

def check(n):
	return isPalin(n) and isSqPalin(n)

tcs=int(input())

for tc in range(1,tcs+1):
	line = input()
	nums=line.split()
	count = 0
	# print (nums[0]+" "+nums[1])
	for i in range(int(nums[0]),int(nums[1])+1):
		if check(i):
			#print ("\t"+str(i))
			count += 1
	print ("Case #"+str(tc)+": "+str(count))

