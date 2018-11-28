from math import sqrt, ceil, floor
def is_palindrome(n):
    if n < 10:
        return True
    s = str(n)
    s2 = s[::-1]
    if s==s2:
        return True
cases = int(raw_input())

for t in range(cases):
    count = 0
    interval = raw_input().split(' ')
    low = long(ceil(sqrt(long(interval[0]))))
    high = long(floor(sqrt(long(interval[1]))))
    
    for n in xrange(low, high+1):
        if is_palindrome(n):
            if is_palindrome(n**2):
                count += 1
    print "Case #%d: %d" %(t+1, count)