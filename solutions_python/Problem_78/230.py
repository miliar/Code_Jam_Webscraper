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
def minGames(percent,n):
    for i in xrange(1,n+1):
        if percent * i % 100 == 0:
            return i
    return None

for _ in xrange(int(raw_input())):
    n, pd, pg = (int(x) for x in raw_input().split())
    d = minGames(pd,min(n,100))
    if d is not None and (pg < 100 or pd == 100) and (pg > 0 or pd == 0):
        gout('Possible')
    else:
        gout("Broken")
