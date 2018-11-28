import sys

def mdc(a, b):
    if a > b:
        return mdc(b,a)
    if a == 0:
        return b
    return mdc(b%a, a)

if __name__ == '__main__':
    C = input()
    for caseID in xrange(C):
        s = raw_input()
        numbers = s.split(" ")
        N = int(numbers[0])
        L = []
        for i in xrange(N):
            for j in xrange(i+1, N):
                n1, n2  = int(numbers[i+1]), int(numbers[j+1])
                delta = abs(n1 - n2)
                L += [delta]
        m = L[0]
        for i in xrange(1,len(L)):
            m = mdc(L[i], m)
        t1 = int(numbers[1])
        print "Case #%d: %d"%(caseID+1, ((t1/m+1)*m - t1)%m)
        
        
            
                
                
        
