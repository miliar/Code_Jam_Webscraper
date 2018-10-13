from fractions import gcd


def apo(L,N):
    
    i = 1
    K = []
    while i<N:
        K.append(abs(L[i] - L[i-1]))
        i += 1
    T = reduce(gcd,K)
    r = L[0] % T
    if r:
        return T- r
    return 0


with open('B-large.in') as infile:
    C = int(infile.readline())
    with open('B-large.out','w') as outfile:
        j = 1
        while j<=C:
            lst = map(int, infile.readline().split())
            N, L = lst[0], lst[1:]
            outfile.write('Case #%d: %d\n' %(j,apo(L,N)))
            j += 1

    
