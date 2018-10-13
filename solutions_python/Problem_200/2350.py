T = int(raw_input())
for case in range(T):
    N = map(int, list(raw_input()))
    L = len(N)
    left = L
    for i in range(L-1, 0, -1):
        if N[i-1] > N[i]:
            left = i
            N[i-1] -= 1
    
    start = 1 if N[0] == 0 else 0
    ans = ''.join(map(str, N[start:left])) + '9'*(L - left)
    print 'Case #%d: %s' % (case+1, ans)
