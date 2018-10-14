T = input()
for t in xrange(T):
    N = input()
    S = map(int, str(N))
    L = len(S)
    
    if L == 1:
        print 'Case #{}: {}'.format(t + 1, N)
    else:
        for i in xrange(L - 1):
            if S[i] > S[i + 1]:
                j = i
                while j >= 0 and S[j] > S[j + 1]:
                    S[j + 1] = 9
                    S[j] -= 1
                    j -= 1
                for k in xrange(j + 2, L):
                    S[k] = 9
                break
        
        print 'Case #{}: {}'.format(t + 1, ''.join(map(str, S)).replace('0', ''))
