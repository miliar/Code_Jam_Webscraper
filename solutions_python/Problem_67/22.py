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

def tick(l):
    new = []
    old = []
    for i,j in l:
        if (i-1,j) not in l and (i,j-1) not in l:
            old.append((i,j))
        if (i+1,j) not in l and (i+1,j-1) in l:
            new.append((i+1,j))
    for i,j in new:
        l.add((i,j))
    for i,j in old:
        l.remove((i,j))
    return l

for _ in xrange(int(raw_input())):
    r = int(raw_input())
    l = set()
    for _ in xrange(r):
        x1,y1,x2,y2 = (int(x) for x in raw_input().split())
        for i in xrange(x1,x2+1):
            for j in xrange(y1,y2+1):
                l.add((i,j))
    i = 0
    while l:
        i += 1
        l = tick(l)
    gout(i)
