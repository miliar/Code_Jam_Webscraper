



def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def nextPerm(a):
    if len(a) <= 1: return False; 
    i = len(a) - 1
    while (a[i - 1] >= a[i]):
        i -= 1
        if i == 0: return False
    j = len(a)
    while (a[j - 1] <= a[i - 1]):
        j -= 1
        if (j == 0): return False; 
    swap(a, i - 1, j - 1); 
    i += 1; 
    j = len(a)
    while (i < j):
        swap(a, i - 1, j - 1); 
        i += 1
        j -= 1
    return True; 


def permute(S, P):
    return ''.join(''.join(S[i+k] for i in P) for k in range(0, len(S), len(P)))
    

def compress(S):
    l = S[0]
    r = 1
    for i in S:
        if i != l:
            r += 1
            l = i
    return r

def main():
    
    
    C = int(raw_input())
    for c in xrange(C):
        
        
        K = int(raw_input())
        S = raw_input()
        
        P = range(K)
        r = compress(permute(S,P))
        
        while nextPerm(P):
            #print P
            t = compress(permute(S,P))
            if t < r:
                r = t
            
            
            
        #print len(S)
        assert len(S) >= r
        
        print 'Case #%d: %d' % (c+1, r)
        







if __name__ == '__main__':
    main()