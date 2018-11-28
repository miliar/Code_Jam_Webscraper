import math
with open('C-small.in') as f:
    num_cases = int(f.readline().replace('\n', ''))    

    for case in xrange(1, num_cases+1):
        count = 0
        n, m = [ int(x) for x in f.readline().replace('\n','').split() ]
        n = int(math.ceil(math.sqrt(n)))
        m = int(math.floor(math.sqrt(m)))
        
        for x in xrange(n,m+1):
            p = str(x)
            if p != p[::-1]:
                continue
                
            sq = str(x*x)
            if sq == sq[::-1]:
                count = count + 1
        print "Case #%d: %d" % (case, count)
