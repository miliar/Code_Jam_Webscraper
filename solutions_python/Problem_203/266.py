tnum = int(raw_input())

def f(s):
    if s=='?'*len(s):
        return s
    s = list(s)
    x = '?'
    for i in range(len(s)):
        if s[i]!='?':
            x = s[i]
        s[i]=x
    for i in reversed(range(len(s))):
        if s[i]!='?':
            x = s[i]
        s[i] = x
    return ''.join(s)

for ti in range(tnum):
    n, m = [int(x) for x in raw_input().split()[:2]]
    S = [raw_input().strip() for _ in range(n)]
    S = [f(s) for s in S]
    x = '?'*m
    for i in range(len(S)):
        if S[i]!='?'*m:
            x = S[i]
        S[i]=x
    for i in reversed(range(len(S))):
        if S[i]!='?'*m:
            x = S[i]
        S[i]=x
    print 'Case #{}:'.format(ti+1)
    for s in S:
        print s
