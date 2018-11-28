import sys, string
import time

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

digits = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"];

def try_digit(digit, S, C):
    S0 = S
    C0 = [x for x in C]
    S = [c for c in S]
    try:
        for c in digits[digit]:
            i = S.index(c)
            C[i] += 1
            S[i] = S[i].lower()
    except:
        return False, S0, C0
    S = "".join(S)
    return True, S, C

def min_count(digit, S, C):
    count = 1e10
    for c in digits[digit]:
        i = S.index(c)
        count = min(count, C[i])
    return count

T = readint()
for t in range(T):
    S = sys.stdin.readline().strip()
    
    #~ if t != 3: continue
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    
    #~ print S
    C = [0] * len(S)
    d = 0
    digs = []
    while min([ord(x) for x in S]) <= ord('Z'):
        # do only non-ambiguous cases
        ok = [False] * 10
        for x in range(10):
            ok[x], Sx, C = try_digit(x, S, C)
        #~ print ok
        #~ print C
        for x in range(10):
            if ok[x]:
                if min_count(x, S, C) == 1:
                    digs.append(x)
                    k, S, C = try_digit(x, S, C)
                    assert(k)
                    break
        C = [0 for x in C]
        
        #~ break
        #~ print S
    digs.sort()
    digs = [str(x) for x in digs]
    print "".join(digs)
