N = input()
for n in xrange(N):
    A, K = raw_input().split()
    K = int(K)
    count = 0
    A = [+(a == '+') for a in A]
    for i in xrange(len(A)):
        a = A[i]
        if a == 0:
            if i > len(A) - K:
                print 'Case #{}: IMPOSSIBLE'.format(n + 1)
                break
            count += 1
            for k in xrange(1, K):
                A[i + k] = 1 - A[i + k]
    else:
        print 'Case #{}: {}'.format(n + 1, count)
