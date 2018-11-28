SIZE    = 'large' # 'small'
INPUT   = 'd-' + SIZE + '.in'
OUTPUT  = 'd-' + SIZE + '.out'

DATASET = []
RESULT  = []

def read_input():
    with open(INPUT) as infile:
        T = int( infile.readline() )
        for t in xrange(T):  # @UnusedVariable
            infile.readline() # skip number of blocks
            
            line   = infile.readline()
            naomis = [ int( float(x) * 100000 ) for x in line.strip().split() ]
            
            line   = infile.readline()
            kens   = [ int( float(x) * 100000 ) for x in line.strip().split() ]
            
            DATASET.append( (sorted(naomis), sorted(kens)) )

def write_result():
    C = 0
    with open(OUTPUT, 'w') as outfile:
        for n, k in RESULT:
            C = C + 1
            rline = 'Case #%d: %d %d' % (C, n, k)
            
            print rline
            outfile.write(rline)
            outfile.write('\n')

def solve():
    for naomis, kens in DATASET:
        deceitful_war, war = 0, 0
        
        # war
        wn = list(naomis)
        wk = list(kens)

        def smallest_larger(lst, num): # based on bisect_right
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo+hi)//2
                if num < lst[mid]: hi = mid
                else: lo = mid+1
            return lo
        
        for n in wn:
            ki = smallest_larger(wk, n)
            if ki < len(wk):
                wk = wk[0:ki] + wk[ki+1:]
            else:
                wk = wk[1:]
                war += 1
                
        # deceitful war
        for n in naomis:
            if n < kens[0]:
                kens = kens[0:-1]
            else:
                kens = kens[1:]
                deceitful_war += 1
                
        RESULT.append( (deceitful_war, war) )

if __name__ == '__main__':
    read_input()
    solve()
    write_result()
    