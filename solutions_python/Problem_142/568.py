import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        numstrs = int(f.readline())
        
        strs = []
        counts = []
        for i in xrange(numstrs):
            line = f.readline().strip("\r\n") + "."
            prev = line[0]
            n = 1
            s = ""
            co = []
            for c in line[1:]:
                if c != prev:
                    s += prev
                    co.append(n)
                    
                    n = 1
                    prev = c
                else:
                    n += 1
                    
            # print s
            # print co
            
            strs.append(s)
            counts.append(co)
            
        eq = True
        for i in xrange(numstrs-1):
            if strs[i] != strs[i+1]:
                eq = False
                break
                
        if not eq:
            res = "Fegla Won"
        else:
            summ = 0
            for i in xrange(len(strs[0])):
                low = 1000
                for target in xrange(200):
                    total = 0
                    for j in xrange(numstrs):
                        total += abs(target - counts[j][i])
                        
                    low = min(low, total)
            
                #print i, low
                summ += low
            res = str(summ)
            
        print "Case #%d: %s" % (caseno+1, res)
        
main()