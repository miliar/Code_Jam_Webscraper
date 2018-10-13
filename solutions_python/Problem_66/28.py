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
'''
def newleft(left):
    new = []
    for i in xrange(len(left)/2):
        new.append(min(left[2*i],left[2*i+1]))
    return tuple(new)'''

def newprices(prices):
    l = []
    r = []
    n = (len(prices)+1)/4
    i = 0
    while n >= 1:
        l.extend(prices[i:i+n])
        r.extend(prices[i+n:i+n+n])
        i += 2*n
        n /= 2
    return (tuple(l),tuple(r))

@memoize
def cheapest(prices,*left):
    
    if len(prices) == 0: return 0

    lp,rp = newprices(prices)
    val = cheapest(lp,*(tuple(left[:len(left)/2]))) + cheapest(rp,*(tuple(left[len(left)/2:]))) + prices[-1]
    if all(left):
        newleft = [i-1 for i in left]
        newval = cheapest(lp,*(tuple(newleft[:len(left)/2]))) + cheapest(rp,*(tuple(newleft[len(left)/2:])))
        if newval < val: return newval
    return val

for _ in xrange(int(raw_input())):
    depth = int(raw_input())
    left = [int(x) for x in raw_input().split()]
    #print left
    prices = []
    for _ in xrange(depth):
        prices.extend(int(x) for x in raw_input().split())
    gout(cheapest(tuple(prices),*left))
