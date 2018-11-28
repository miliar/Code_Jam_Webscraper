import math

def ispalindrome(n):	# ok, didn't really need this, but since i wrote it i might as well use it
	digits = [int(x) for x in str(n)]
	length = len(digits)

	# if even number of digits, we want to compare the first half to the second half
	# if odd, we don't want to compare the middle to itself, so the truncating should be perfect
	for i in range(length/2):
		if digits[i] != digits[length-i-1]:
			return 0
	return 1
	
def getnextpal(n):
	digits = [int(x) for x in str(n)]
	length = len(digits)
	digits = [0] + digits # extra digit in case of overflow
	
	for i in range(length/2):
		x = i + 1
		y = length-i
		#print "{} {}... {} {}".format(x, y, digits[x], digits[y])
		if digits[x] > digits[y]:
			digits[y] = digits[x]
		elif digits[x] < digits[y]:	
			# find next incremental digit to the left of y, and increment it			
			# the leftmost possible z is x. x cannot be 9 (not incrementable), because digits[x] < digits[y]
			z = y - 1				
			while digits[z] == 9:
				z -= 1
			digits[z] += 1
			#now y is free to be any digit
			digits[y] = digits[x]
			#but we have to zero out the digits in between
			for k in range(z+1,y):
				digits[k] = 0
		# else equal, in which case keep going
		
	return int("".join(str(x) for x in digits))

def fairsquare(A,B):
	fscount = 0
	minroot = int(math.ceil(math.sqrt(A))) 	# minimum val that you can square to get A
	nextpal = getnextpal(minroot)
	nextsquare = nextpal * nextpal
	
	while(nextsquare) <= B:
		if ispalindrome(nextsquare):
			fscount += 1
		nextpal = getnextpal(nextpal+1)
		nextsquare = nextpal * nextpal
		
	return fscount
	

f = open('C-large-1.in', 'r')
T = int(f.readline())
for i in range(T):
	nums = f.readline().split(' ')
	A = int(nums[0])
	B = int(nums[1])	
	print "Case #{}: {}".format(i+1, fairsquare(A,B))