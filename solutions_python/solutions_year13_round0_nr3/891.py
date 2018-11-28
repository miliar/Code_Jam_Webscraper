import math
def ispalindrome(n):
    a = str(n)
    for i in xrange(len(a)/2):
        if a[i] != a[len(a)-1-i] :
            return False
    return True


s = []
for i in xrange(1,10000001):
    if ispalindrome(i) and ispalindrome(i*i):
        s.append(i*i)

t = int(raw_input())
for ab in xrange(t):
    count = 0
    x = raw_input()
    x = map(int,x.split())
    a = x[0]
    b = x[1]
    for i in xrange(len(s)):
        if s[i] >= a and s[i] <= b:
             count += 1
    print "Case #%d: %d" % (ab+1,count)
    
