from collections import defaultdict

def solve(comb_dict, opp_dict, invocations):
    elements = []
    for e in invocations:
       elements.append(e)
       created = comb_dict.get(tuple(elements[-2:]))
       if created:
           #print '-', elements
           #print elements[-2:], '->', created
           elements[-2:] = created
       elif any(opp in elements for opp in opp_dict[e]):
           #print 'POOF', elements
           del elements[:]
       #print elements
       
    return elements
    
def format(elements):
    return '[%s]' % (', '.join(c for c in elements))

T = int(raw_input())

for t in xrange(1, T+1):
    ws = iter(raw_input().split())
    combinations = (ws.next() for _ in xrange(int(ws.next())))
    comb_dict = {}
    for b1, b2, nb in combinations:
        comb_dict[(b1, b2)] = nb
        comb_dict[(b2, b1)] = nb

    oppositions = (ws.next() for _ in xrange(int(ws.next())))
    opp_dict = defaultdict(list)
    for b1, b2 in oppositions:
        opp_dict[b1].append(b2)
        opp_dict[b2].append(b1)
        
    ws.next()
    invocations = ws.next()
    solution = solve(comb_dict, opp_dict, invocations)
    print "Case #%d: %s" % (t, format(solution))
