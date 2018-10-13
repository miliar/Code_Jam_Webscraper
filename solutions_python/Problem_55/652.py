import psyco
psyco.full()

def main():
    f = open('C-small-attempt0.in')
    fo = open('C-small.out','w')

    T = int(f.next().strip())

    for t in xrange(T):
        R,k,N = [int(x) for x in f.next().strip().split()]
        gs = [int(x) for x in f.next().strip().split()]
        
        i = 0
        grandtot = 0
        for Rnum in xrange(R):
            tot = gs[i]
            starti = i
            
            while tot <= k:
                i += 1
                if i == N:
                    i = 0
                tot += gs[i]
                if i == starti:
                    break
                
            
            tot -= gs[i]
            grandtot += tot
        fo.write('Case #%d: %d\n' % (t+1,grandtot))
    f.close()
    fo.close()
            
            
main()
        
