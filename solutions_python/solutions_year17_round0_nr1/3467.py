def flip(S, i, k):
    for j in xrange(k):
        if S[i+j] == '+':
            S[i+j] = '-'
        elif S[i+j] == '-':
            S[i+j] = '+'
    return S

def allHappy(S):
    for c in S:
        if c != '+':
            return False
    return True
T = int(raw_input())
for t in xrange(T):
    S,k = raw_input().split(' ')
    S = list(S)
    k = int(k)
    cnt = 0;
    for i in xrange(len(S)-k+1):
        c = S[i]
        if c == '-':
            S = flip(S,i,k)
            cnt+=1
    if allHappy(S):
        print "Case #{0}: {1}".format(t + 1, cnt)
    else:
        print "Case #{0}: {1}".format(t + 1, "IMPOSSIBLE")