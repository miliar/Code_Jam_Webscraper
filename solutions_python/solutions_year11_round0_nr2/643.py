import sys

f = open(sys.argv[1])
output_file = sys.argv[1].replace("in", "out")
output = open(output_file, "w")
T = int(f.readline().strip())

for i in xrange(T):
    print "Case ", (i + 1)
    s = f.readline().strip().split(" ")
    C = int(s[0])

    rewrite = {}
    opposed_set = {}
    current = 1
    for c in xrange(C):
        x = s[current]
        current += 1
        a = x[0]
        b = x[1]
        if a not in rewrite:
            rewrite[a] = {}
        if b not in rewrite:
            rewrite[b] = {}
        rewrite[a][b] = x[2]
        rewrite[b][a] = x[2]
    D = int(s[current])
    current += 1
    for d in xrange(D):
        x = s[current]
        current += 1
        a = x[0]
        b = x[1]
        if a not in opposed_set:
            opposed_set[a] = []
        if b not in opposed_set:
            opposed_set[b] = []
        opposed_set[a].append(b)
        opposed_set[b].append(a)    
        
    print "Rewrite", rewrite
    print "Opposed", opposed_set
    
    N = int(s[current])
    current += 1
    print N
    l = []

    cards = s[current]
    print "Cards", cards
    for card in cards:
        print "[%s], %s" % (",".join(l), card)

        rewritten = False
        opposed = False
        if len(l) > 0:
            while True:        
                last_card = l[-1]
                if last_card in rewrite and card in rewrite[last_card]:
                    del l[-1]
                    l.append(rewrite[last_card][card])
                    rewritten = True
                    print "Rewrite", l
                else:
                    break
                        
        
        if not rewritten and (card in opposed_set):
            for opp_pair in opposed_set[card]:
                if opp_pair in l:
                    print "Clear"
                    l = []
                    opposed = True
        
        if not rewritten and not opposed:
            l.append(card)
    
    o = "Case #%s: [%s]\n" % (i + 1, ", ".join(l))
    print o,
    output.write(o)
        
    