_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

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
def maxVal(candy, myVal=0, hisVal=0, myWeight=0, hisWeight=0):
    if not candy:
        if myWeight==hisWeight and hisVal>0:
            return myVal
        else:
            return None
    
    toMe = maxVal(tuple(candy[1:]), myVal+candy[0], hisVal, myWeight^candy[0], hisWeight)
    toHim = maxVal(tuple(candy[1:]), myVal, hisVal+candy[0], myWeight, hisWeight^candy[0])
    
    if toMe is None:
        return toHim
    elif toHim is None:
        return toMe
    else:
        return max(toMe,toHim)

for _ in xrange(int(raw_input())):
    raw_input()
    candy = tuple((int(x) for x in raw_input().split()))
    maxVal = sum(candy) - min(candy)
    cur = 0
    for c in candy:
        cur ^= c
    gout("NO" if cur else maxVal)
    #result = maxVal(candy)
    #gout("NO" if result is None else result)
    
