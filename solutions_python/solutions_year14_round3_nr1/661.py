import sys 

def do(p, q):
    cnt = 0 
    while q > p:
        if q%2 != 0: return  "impossible"
        q /= 2
        cnt += 1 
    return cnt       

def do1(p, q):
    cnt = 0 
    cnt1 = 0 
    while q != 1:
        if q == p: return cnt 
        if q%2 != 0: return  "impossible"
        if q > p: cnt += 1 
        cnt1 += 1 
        q /= 2
    return cnt 
#print do1(3,4)
#print do1(1,4)
#sys.exit()
#print do(3,["aabc", "abbc", "abcc"])
t = int(raw_input())
for i in xrange(t):
    p,q = map(int, raw_input().split("/"))
    print "Case #{}: {}".format(i+1,do1(p,q))
