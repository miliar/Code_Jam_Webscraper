def f(K,N):
    if(N==K):
        return (0,0)
    if N == 1:
        return ((K-1)//2 + ((K-1)&1), (K-1)//2)
    if (N-1) & 1 == 0:
        return f((K-1)//2, (N-1)//2)
    else:
        return f((K-1)//2 + ((K-1)&1), (N-1)//2 + ((N-1)&1))

print(f(3,1))

fin = open('c3.in')
fout = open('c3.out', 'w')

T = int(fin.readline())

for t in range(1, T+1):
    [K,N] = [int(x) for x in fin.readline().split(' ')]
    a,b = f(K, N)
    fout.write('Case #%s: %s %s\n' % (t, a, b))
