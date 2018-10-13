import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        nweights = int(f.readline())
        
        weights = []
        
        for w in f.readline().strip().split():
            weights.append((float(w), "N"))
            
        for w in f.readline().strip().split():
            weights.append((float(w), "K"))
        
        weights.sort()
        
        # for w in weights:
            # print w
        # print
        
        diff = 0
        wins = 0
        for w, p in weights:
            if p == "N":
                diff += 1
            elif p == "K":
                if diff > 0:
                    diff -= 1
                else:
                    wins += 1
                    
        diff = 0
        loss = 0
        for w, p in weights:
            if p == "K":
                diff += 1
            elif p == "N":
                if diff > 0:
                    diff -= 1
                else:
                    loss += 1
                
        wins2 = nweights - loss
        print "Case #%d: %d %d" % (caseno+1, wins2, wins)
        
main()