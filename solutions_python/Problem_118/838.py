import math
fd = file('C-large-1.in')
totalTestCase = int(fd.readline())
memoizeTbl = {}
def genTestCase(fd):
    global totalTestCase
    while totalTestCase > 0:
        (lowerBound, upperBound) = [int(x) for x in fd.readline().strip().split()]
        totalTestCase -= 1
        yield (lowerBound, upperBound)
    fd.close()

def panlidrome(n_str):
    if len(n_str) == 1:
        return True
    half_len = len(n_str) / 2
    lower_half = n_str[0:half_len]
    upper_half = n_str[len(n_str)-half_len:]
    if lower_half == upper_half[::-1]:
        return True
    else:
        return False
tc_seq = 1
for (lb, ub) in genTestCase(fd):
    f_and_s = 0
    lb_square = math.ceil( math.sqrt( lb ) )
    ub_square = math.floor( math.sqrt( ub ) )
    #isPartialMemoized = False
    '''
    for n_square in xrange( int( lb_square ), int( ub_square )+1):
        mem_low_idx = int( math.log10(lb_square).floor() )
        mem_high_idx = int( math.log10(ub_square).ceil() )
        n_square_str = str(n_square)
        n_str = str(n_square*n_square)
        #print '\t', n_square
        if panlidrome(n_square_str) and panlidrome(n_str):
            print '\t\t', n_str
            if not isMemoized:
                idx =  
            f_and_s += 1
    '''
    mem_low_idx = int( math.floor(math.log10(lb_square)) )
    mem_high_idx = int( math.ceil(math.log10(ub_square)) )
    temp = []
    if mem_low_idx == mem_high_idx or mem_high_idx == 0:
        mem_high_idx += 1
    for n in xrange(mem_low_idx, mem_high_idx):
        #print mem_low_idx, mem_high_idx
        if n not in memoizeTbl:
            memoizeTbl[n] = []
            for n_square in xrange( 10**n, 10**(n+1)+1):
                n_square_str = str(n_square)
                n_str = str(n_square*n_square)
                #print '\t', n_square
                if panlidrome(n_square_str) and panlidrome(n_str):
                    #print '\t\t', n_str
                    #f_and_s += 1
                    memoizeTbl[n].append(int(n_str))
        temp.extend(memoizeTbl[n])
    #print temp
    f_and_s = len([x for x in temp if lb <= x <= ub])
    print 'Case #%d: %d'%(tc_seq, f_and_s)
    tc_seq += 1
    
