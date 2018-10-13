import sys, string
import time

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def solve(S):
    try:
        i = S.index("?")
    except:
        S = "".join(S)
        #~ print S
        c,j = S.split(" ")
        c = int(c)
        j = int(j)
        #~ print c,j
        return S, abs(c-j), c, j
    
    min_mad = 1e100
    min_c = 1e100
    min_j = 1e100
    sol = None
    
    for d in range(10):
        S[i] = str(d)
        Sx,mad,c,j = solve([c for c in S])
        if mad < min_mad:
            min_mad, min_c, min_j = mad, c, j
            sol = Sx
        elif mad == min_mad and c < min_c:
            min_c, min_j = c, j
            sol = Sx
        elif mad == min_mad and c == min_c and j < min_j:
            min_j = j
            sol = Sx
    return sol, min_mad, min_c, min_j

T = readint()
for t in range(T):
    S = sys.stdin.readline().strip()
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),
    #~ print S
    sol, min_mad, min_c, min_j = solve([c for c in S])
    print sol
    #~ print min_mad, min_c, min_j
