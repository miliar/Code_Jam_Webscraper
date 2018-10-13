import sys, math

data = sys.argv[1]

f = open(data,'r')
data = f.read()

tests = data.split("\n")

# Cut the first and last lines off
tests = tests[1:len(tests)-1]


case = 0
done = False
row = 0

def isPalindrome(i):
	list = []
		
	for char in str(i):
		list.append(char)
		
	list.reverse()
	list = "".join(list)
	
	return list == str(i)
		

for test in tests:
	case += 1
	count = 0
	(low, high) = test.split(" ")
	for i in range(int(low),int(high)+1):
		if isPalindrome(i) and int(math.sqrt(i)) == math.sqrt(i) and isPalindrome(int(math.sqrt(i))):
			#print "%s is a palindrome" % (i)
			count += 1


	result = count
	print "Case #%s: %s" % (case, result)
		
	