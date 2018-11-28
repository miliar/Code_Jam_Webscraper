
import math

l = [0 for i in range(20)]

def test(n):
    ret = 0
    res = 0
    for i in range(n):
	res *= 10
        res += l[i]
    
    start = str(res)
    temp = start
    for i in xrange(n - 1, -1, -1):
	temp += start[i]
    num1 = int(temp)
    if num1:
    	p = num1 * num1
    	p2 = str(p)
    	if p2 == p2[::-1]:
#            print num1, p
            if p >= a and p <= b:
		ret += 1

    for i in xrange(0, 4):
	temp = start + str(i)
    	for i in xrange(n - 1, -1, -1):
            temp += start[i]
        num1 = int(temp)
    	if num1:
            p = num1 * num1
            p2 = str(p)
            if p2 == p2[::-1]:
 #           	print num1, p
	       	if p >= a and p <= b:
                    ret += 1
    return ret

ans = 0

def gen(ind, n):
    global ans
    if ind == n:
	ans += test(n)
	return 
    for i in range(0, 3):
	if ind == 0 and i == 0:
            continue
	l[ind] = i
	gen(ind + 1, n)
	l[ind] = 0


test2 = int(raw_input())
for t in xrange(test2):
    ans = 0
    a, b = map(int, raw_input().split(" "))
    for i in range(0, 3):
	gen(0, i)
    print "Case #" + str(t + 1) + ": " + str(ans)

