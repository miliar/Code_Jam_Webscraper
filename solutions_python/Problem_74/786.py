import sys
def main():
    file = sys.argv[1]
    f = open(file, 'r')
    cases = int(f.readline())
    
    for case in xrange(cases):
        seq = f.readline().split()
        bots, locations = seq[1::2], seq[2::2]
        place = {'O' : 1, 'B' : 1}
        last = bots[0]
        last_cost = 0
        total = 0
        for turn,loc in zip(bots,locations):
            loc = int(loc)
            cost = abs(loc - place[turn])
            if last != turn:
                # if we were not last to go, then we made up to last_cost moves
                # simultaneously
                cost -= last_cost
                cost = max(cost, 0)
                last_cost = 0

            total += cost + 1
            last_cost += cost + 1
            place[turn] = loc
            last = turn
        
        print "Case #%d: %d" % (case + 1, total)
            
        
        
     
if __name__ == "__main__":
    sys.exit(main())
