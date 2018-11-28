OUTP_FORMAT = "Case #{}: {}"
IMPOSSIBLE = "IMPOSSIBLE"

def switch(C):
    if C == '+':
        return '-'
    else:
        return '+'

def solver(S, K):
    res = 0
    SL = list(S)
    L = len(S)
    for i, s in enumerate(SL):
        if s == '-':
            if i + K > L:
                return IMPOSSIBLE 
            for x in xrange(i, i + K):
                SL[x] = switch(SL[x])
            res += 1
    return res 

T = int(raw_input().strip())

for index in xrange(T):
    S, K  = raw_input().strip().split()
    K = int(K)
    print OUTP_FORMAT.format(index + 1, solver(S, K))
