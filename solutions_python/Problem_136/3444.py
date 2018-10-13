import sys
sys.stdin = open("B.in")
sys.stdout = open("B.out","w")
T = input()
for i in range(T):
    print "Case #%d:"%(i+1),
    C, F, X = map(lambda x: float(x), raw_input().split())
    r = 2.0;
    base = 0.0;
    ans = X/r
    while True:
        #~ print r, ans
        base += C/r
        r += F
        if (ans - (base+X/r) > 0.00000001):
            ans = base+X/r
        else:
            break
    print "%.7f" % ans
    
