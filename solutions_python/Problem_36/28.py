def memoize(f):
    dict = {}
    def func(*n):
	if n in dict:
	    return dict[n]
	else:
	    dict[n] = f(*n)
	    return dict[n]
    return func

str = "welcome to code jam"

@memoize
def getNums(s,p):
    if p[0] != s[0]: return 0
    if len(s) == 1: return 1
    sum = 0
    for i in xrange(1,len(p)):
        if getNums(s[1:],p[i:]):
            if not sum: sum = getNums(s[1:],p[i:])
            else: sum += getNums(s[1:],p[i:])
    #print s,p,sum
    return sum % 10000

n = int(raw_input())
for i in xrange(n):
    p = raw_input()
    sum = 0
    for j in xrange(len(p)):
        if getNums(str,p[j:]):
            if not sum: sum = getNums(str,p[j:])
            else: sum += getNums(str,p[j:])
    
    print "Case #%d: %04d" % (i+1,sum % 10000)


