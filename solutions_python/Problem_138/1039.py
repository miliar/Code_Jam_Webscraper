import sys
import time
import operator

with open(sys.argv[1]) as file:
    t = int(file.readline())
    for n in range(1,t+1):
        b = int(file.readline())
        naomi = sorted(map(float,file.readline().split()))
        ken = sorted(map(float,file.readline().split()))
        
#         debug = []
#         debug += [("N",w) for w in naomi]
#         debug += [("K",w) for w in ken]
#         print [a for a,v in sorted(debug,key=operator.itemgetter(1))]
        
        
        
        o_ken = ken[:]
        war_score = 0
        for w in naomi:
            if max(o_ken) > w:
                o_ken.remove(min((k for k in o_ken if k > w)))
            else:
                o_ken.remove(min(o_ken))
                war_score += 1
        dw_score = 0        
        for w in naomi:
            min_ken = min(ken)
            max_ken = max(ken)
            if  w > min(ken):
                ken.remove(min_ken)
                dw_score += 1
            else:
                ken.remove(max(ken))
        print "Case #%d: %d %d" % (n,dw_score,war_score)
        