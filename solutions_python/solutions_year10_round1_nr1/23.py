import sys

def test(S, k):
    #print "test %s, %d" % (S, k)
    r_ok = 0
    if S.find("R"*k) >= 0:
        r_ok = 1
    b_ok = 0 
    if S.find("B"*k) >= 0:
        b_ok = 1
    return (r_ok, b_ok)

getline = sys.stdin.readline

def tc(I):
    N, K = [int(x.strip()) for x in getline().split()]
    
    P = []
    for _ in xrange(N):
        line = getline().strip().replace(".","").rjust(N, ".")
        #print "line: %s" % line
        P.append(line)
    
    red = 0
    blue = 0
    
    for r in xrange(N):
        S1 = ""
        S2 = ""
        S3 = ""
        S4 = ""
        S5 = ""
        S6 = ""
    
        for c in xrange(N):
            S1 += P[r][c]
            S2 += P[c][r]
            if r+c < N:
                S3 += P[c][r+c]
                S4 += P[r+c][c]
                S6 += P[N-c-1][r+c]
            if r-c >= 0:
                S5 += P[c][r-c]
    
        for S in (S1, S2, S3, S4, S5, S6): 
            (r, b) = test(S, K)
            red += r
            blue += b
    
    res = "Neither"        
    if red > 0 and blue > 0:
        res = "Both"
    elif red > 0:
        res = "Red"
    elif blue > 0:
        res = "Blue"
    print "Case #%d: %s" % (I, res)
               
T = int(getline()) 
for i in range(T):
    tc(i+1)
