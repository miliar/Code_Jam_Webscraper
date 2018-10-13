ccc = -1
def check(t, S, K) :
    s = list(S)
    for i in t :
        for j in range(i-K+1, i+1) :
            if s[j] == '-' : s[j] = '+'
            else : s[j] = '-'
    s = ''.join(s)
    if len(s) == s.count('+') : return len(t)
    return -1
def combi(a, b, c, t, S, K) :
    global ccc
    if c == 0 :
        x = check(t, S, K)
        if x != -1 : ccc = x
        return
    for i in range(a, b) :
        t.append(i)
        combi(i+1, b, c-1, t, S, K)
        if ccc != -1 : return
        t.pop()
def solve(S, K) :
    global ccc
    if S.count('+') == len(S) : return '0'
    for i in range(1, len(S)+1) :
        t = list()
        combi(K-1, len(S), i, t, S, K)
        if ccc != -1 : return str(ccc)
    return "IMPOSSIBLE"
T = int(input())
for t in range(T) :
    S, K = input().split()
    K = int(K)
    ccc = -1
    ans = solve(S,K)
    print("Case #", t+1, ': ', ans, sep='')
