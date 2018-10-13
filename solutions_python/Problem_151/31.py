import sys, itertools


import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        a,b = f.readline().strip("\r\n").split()
        nwords = int(a)
        nservers = int(b)
            
        words = []
        stats = {}
        largest = -1
        
        for i in xrange(nwords):
            words.append(f.readline().strip("\r\n"))
            
        for p in itertools.product(range(nservers), repeat=nwords):
        
            count = 0
            for sno in xrange(nservers):
                storeds = {}
                
                for i in xrange(nwords):
                    if p[i] == sno:
                        w = words[i]
                        
                        for j in xrange(0, len(w)+1):
                            segment = w[0:j]
                            storeds[segment] = True
                            
                count += len(storeds)
                
            if count not in stats:
                stats[count] = 0
            stats[count] += 1
            
            if count > largest:
                largest = count
                
                
                
            
        print "Case #%d: %d %d" % (caseno+1, largest, stats[largest])
        
main()