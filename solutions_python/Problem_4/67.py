def memoize(f):
    dict = {}
    def func(*n):
	if n in dict:
	    return dict[n]
	else:
	    dict[n] = f(*n)
	    return dict[n]
    return func

@memoize
def getMin(v1,v2):
    if len(v1)==0:
        return 0
    minimum = v1[0]*v2[0] + getMin(v1[1:],v2[1:])
    for i in xrange(1,len(v2)):
        cur = v1[0]*v2[i] + getMin(v1[1:],v2[:i]+v2[i+1:])
        if cur<minimum:
            minimum = cur
    return minimum

n = int(raw_input())
for i in xrange(n):
    raw_input()
    v1 = tuple(int(x) for x in raw_input().split())
    v2 = tuple(int(x) for x in raw_input().split())
    print "Case #%d: %d" % (i+1,getMin(v1,v2))
