v = ['a','e','i','o','u']
def count(s,n):
    global v
    i = 0
    while i < (len(s)):
        c = 0
        while s[i] not in v :
            i += 1
            c += 1
            if i == len(s):
                break
        if c >= n :
            return True
        if c == 0:
            i += 1
    return False

t = int(raw_input())
for ab in xrange(1,t+1):
    x = raw_input().split()
    s = x[0]
    n = int(x[1])
    c = 0
    for i in xrange(len(s)-n+1):
        for j in xrange(i+n-1,len(s)):
            if count(s[i:j+1],n):
                c += 1
    print "Case #%d: %d" %(ab,c)
