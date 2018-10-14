

def snap(n,k):
    b = bin(k)[2:]
    if n <= len(b):
        for i in xrange(n):
            if b[i-n] == '0':
                return 'OFF'
        return 'ON'
    return 'OFF'
        



with open('A-large.in') as infile:
    T = int(infile.readline())
    with open('A-large.out','w') as outfile:
        j = 1
        while j<=T:
            n, k = tuple(map(int, infile.readline().split()))
            outfile.write('Case #%d: %s\n' %(j,snap(n,k)))
            j += 1
            
        
    

