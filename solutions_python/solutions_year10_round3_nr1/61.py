

def count(L,N):
    r = 0
    L = sorted(L, key=lambda h:h[0])
    for i in xrange(N-1):
        w = L[i]
        for higher in L[i+1:]:
            if w[1] > higher[1]:
                r += 1
        
    return r



with open('a.in') as infile:
    T = int(infile.readline())
    with open('a.out','w') as outfile:
        j = 1
        while j<=T:
            L = []
            N = int(infile.readline())
            i = 0
            while i<N:
                L.append( tuple(map(int, infile.readline().split())))
                i += 1
            outfile.write('Case #%d: %s\n' %(j,count(L,N)))
            j += 1
            
        
    

