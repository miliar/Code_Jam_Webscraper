#~ def compare(a,b):
    #~ if a[0] < b[0]: return -1
    #~ elif a[0] > b[0]: return 1
    #~ else: return 0

def minutes(x):
    #~ return ( int(x[:2])*60 + int(x[3:]) ) % (24*60)
    return ( int(x[:2])*60 + int(x[3:]) )

def get_orphan_departures( departures, arrivals ):
    result = departures[:]
    #~ print "result: " + str(result)
    for arrival in arrivals:
        dep = [ x for x in result if x >= arrival ]
        if len(dep) > 0:
            #~ print dep[0] 
            result.remove(dep[0])
    return len(result)

for case in xrange(input()):
    tt = int(input())
    na, nb = [int(x) for x in raw_input().split() ]
    #~ print (na, nb)
    table_a = []
    for _ in xrange(na):
        #~ table_a.append( map( lambda x: int(x[:2])*60 + int(x[3:]) , raw_input().split(' ') ) )
        table_a.append( map( lambda x: minutes(x) , raw_input().split(' ') ) )
    #~ print  table_a
    table_b = []
    for _ in xrange(nb):
        table_b.append( map( lambda x: minutes(x) , raw_input().split(' ') ) )
    #~ print  table_b
    
    #~ table_a.sort( compare )
    #~ table_b.sort( compare )

    # then?
    departures_a = [ x[0] for x in table_a ]
    arrivals_a = [ x[1] + tt for x in table_b ]
    departures_a.sort()
    arrivals_a.sort()
    #~ print departures_a, arrivals_a

    #~ print "orphans_a:" + str(get_orphan_departures( departures_a, arrivals_a ))

    departures_b = [ x[0] for x in table_b ]
    arrivals_b = [ x[1] + tt for x in table_a ]
    departures_b.sort()
    arrivals_b.sort()
    #~ print departures_b, arrivals_b

    #~ print "orphans_b:" + str(get_orphan_departures( departures_b, arrivals_b ))
    
    print "Case #%d: %d %d" % ( case + 1, get_orphan_departures( departures_a, arrivals_a ), get_orphan_departures( departures_b, arrivals_b ) )


