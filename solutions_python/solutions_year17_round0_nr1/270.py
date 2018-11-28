T = input()
for t in range(1, T+1):
    s, k = raw_input().split()
    n, k = len(s), int(k)
    b = [int(x == '+') for x in s]
    ans = 0
    for i in range(n-k+1):
        if b[i] == 0:
            ans += 1
            for j in range(i, i+k):
                b[j] ^= 1
    print 'Case #%d:' % t,
    if all(b[i] for i in range(n-k+1, n)):
        print ans
    else: print 'IMPOSSIBLE'
    
            
        

    
    
