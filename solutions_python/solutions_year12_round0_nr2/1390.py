import sys

def answer(N, S, P, scores):
    ans = 0
    for sc in scores:
        if sc == 0 :
            if P == 0:
                ans += 1
            continue
        
        maxp = (sc + 2) / 3
        
        if maxp >= P :
            ans += 1
        elif S > 0:
            maxp = (sc + 4) / 3
            if maxp >= P:
                ans += 1
                S   -= 1
    return ans
    
T = int(sys.stdin.readline())

for caseno in xrange(T):
    line = sys.stdin.readline()
    line = line.strip()
    values = map(lambda x: int(x), line.split(' '))
    N = values[0]
    S = values[1]
    P = values[2]
    scores = values[3:]
    print "Case #%d: %d" % (caseno + 1, answer(N, S, P, scores))
