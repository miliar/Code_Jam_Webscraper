import sys

def main():
    inFile = open(sys.argv[1], 'rt')
    outFile = open(inFile.name.replace('.in', '.out'), 'wt')
#    outFile = sys.__stdout__
    T = int(inFile.readline())
    for t in xrange(1, T+1):
        R,k,N = map(int, inFile.readline().strip().split(' '))
        g = map(int, inFile.readline().strip().split(' '))
        sum = 0
        q = 0
        rides = []
        for i in xrange(R):
            (c, q) = rideOnce(R, k, N, g, q)
            if not (c, q) in rides:
                rides.append((c, q))
                sum += c
            else:
                break
        if i<R:
            # found a cycle
            r0 = rides.index((c, q))
            fullCycles, remaining = divmod(R-r0, len(rides)-r0)
            fullCyclesLeft = fullCycles-1 
            sumCycle = 0
            for j in xrange(r0, len(rides)):
                sumCycle += rides[j][0]   
            sum += sumCycle * fullCyclesLeft  
            for j in xrange(remaining):
                sum += rides[r0+j][0]  
            
        outFile.write('Case #%d: %d\n' % (t, sum))
    outFile.close()
        
def rideOnce(R,k,N,g,q):
    first = q
    c = 0
    while True:
        if c + g[q]>k:
            break
        c += g[q]
        q = (q+1)%N
        if q==first:
            break
    return c, q

if __name__ == '__main__':
    main()
