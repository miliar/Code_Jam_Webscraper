from collections import defaultdict

t = input()

def solve():
    n = input()
    a = map(int,raw_input().split())
    x = reduce(lambda x,y: x^y,a)
    if x!=0: return "NO"
    return sum(a)-min(a)        
    
for i in xrange(t):
    print "Case #%d: %s"%(i+1,solve())
        