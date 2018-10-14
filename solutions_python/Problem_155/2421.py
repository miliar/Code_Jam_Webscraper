f = open('A-large.in')
lines = []

T = int(f.readline())
for t in xrange(T):
    S, A = f.readline().strip('\n').strip('\r').split()
    A = map(int, A)
    B = [0 for _ in xrange(len(A))]

    for i in xrange(1,len(A)):
        B[i] = B[i-1]+A[i-1]
    
    ans = 0
    for i in xrange(1,len(A)):
        if A[i] and B[i]+ans < i:
            ans += i-B[i]-ans

    lines += ['Case #%d: %d' % (t+1, ans)]
    #lines += ['Case #%d: %d %s' % (t+1, ans, ''.join(map(str,A)))]

fout = open('out.txt', 'w')
fout.write('\n'.join(lines))
fout.close()
