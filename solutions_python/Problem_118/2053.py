''' third problem '''

# this is only work for small set.
def palindrome(number):
	num = str(int(number))
	for i in range(len(num)):
		if num[i] != num[len(num)-1-i]:
			return False
	return True

def fairSquare(number):
	if palindrome(number) and palindrome(number**(0.5)):
		return True
	else:
		return False
		
		
MAX = 1001
newmax = 32
T = int(raw_input())
for x in range(T):
	count = 0
	A,B = map(long, raw_input().split())
	for i in range(0, MAX):
		mynum = i**2
		if mynum > B:
			break
		if fairSquare(mynum) and mynum>= A:
			count+=1
					
	print "Case #"+str(x+1)+": "+str(count)
