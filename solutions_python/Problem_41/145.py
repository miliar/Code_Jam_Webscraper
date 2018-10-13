#!/usr/bin/python

def getnext(n):
    k = int(n)
    g = list(n.replace('0', ''))
    g.sort()
    while 1:
         k = k +1
         h = list(str(k).replace('0', ''))
         h.sort()
         if h == g:
             break
    return k

def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][k] = (C[i][k] + A[i][j] * B[j][k]) % 1000
    return C
            
def fast_exponentiation(A, n):
    if n == 1:
        return A
    else:
        if n % 2 == 0:
            A1 = fast_exponentiation(A, n/2)
            return matrix_mult(A1, A1)
        else:
            return matrix_mult(A, fast_exponentiation(A, n - 1))

def readints(f):
    return map(lambda x: int(x), f.readline().strip().split(' '))

if __name__ == '__main__':
    import sys
    inp = open(sys.argv[1], "r")
    
    [N] = readints(inp)
    for i in range(N):
        n = inp.readline().strip()
        print 'Case #%s: %s' % ((i+1), getnext(n))
        
                                
