import math

f = open('C-small.in', 'r')
o = open('C-small.out', 'w')

T = int(f.readline().strip())

def ispalindrome(word):
    return word == word[::-1]

for t in xrange(T):
    (A,B) = map(int, f.readline().strip().split(' '))
    count = 0
    for x in range(A, B+1):
	sqx = math.sqrt(x) 
	if  ispalindrome(str(x)) and sqx ==  int(sqx) and ispalindrome(str(int(sqx))):
		count+=1

    s = "Case #%d: %s\n" % (t+1, count)
    print s
    o.write(s)



