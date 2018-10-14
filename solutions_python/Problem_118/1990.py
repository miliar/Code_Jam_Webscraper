import math

def is_palindrome(w):
    while w and w[0] == w[-1]:
        w = w[1:-1]
    return w == ''

T = int(raw_input())

for test in range(T):
	a,b = raw_input().split()
	a,b=int(a),int(b)
	a,b=int(math.ceil(math.sqrt(a))),int(math.floor(math.sqrt(b)))
	res = 0
	for num in range(a,b+1):
		if is_palindrome(str(num)) and is_palindrome(str(num*num)):
			res = res + 1
	print "Case #" + str(test+1) + ": " + str(res)