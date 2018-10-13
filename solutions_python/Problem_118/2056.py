import math

f = open("./C-small-attempt0.in")
f_out = open('out.txt','w')

num_trials = f.readline()

# intersection function from http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
def intersect(a, b):
     return list(set(a) & set(b))
     
def ispalindrome(number):
	stringnum = str(number)
	return stringnum == stringnum[::-1]
	
for i in range(1, int(num_trials) + 1):
	themin, themax = [int(a) for a in f.readline().strip().split(" ")]
	fulllist = range(themin, themax + 1)
	palindromes = [item for item in fulllist if ispalindrome(item)]
	
	fulllistsmall = range(int(math.floor(math.sqrt(themin))), int(math.ceil(math.sqrt(themax + 1))))
	palindromes_squared = [pow(item, 2) for item in fulllistsmall if ispalindrome(item)]

	f_out.write("Case #%d: %d\n" % (i, len(intersect(palindromes, palindromes_squared))))
	
f.close()
f_out.close()
