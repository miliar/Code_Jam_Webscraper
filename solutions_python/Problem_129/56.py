testcases = int(raw_input())

def prix(n,i):
    return (i*n - (i*(i-1))/2)

for case in xrange(1,testcases+1):
    n,m = raw_input().split()
    n = int(n)
    m = int(m)
    #passagers = []
    stops = set([])
    departs = {}
    arrivees = {}
    sommedue = 0
    for i in xrange(0,m):
        o,e,p = raw_input().split()
        o = int(o)
        e = int(e)
        p = int(p)
        # origine, arrivee, nombre
        #passagers.append([o,e,p])
        stops.add(o)
        stops.add(e)
        if o in departs:
            departs[o] += p
        else:
            departs[o] = p
        if e in arrivees:
            arrivees[e] += p
        else:
            arrivees[e] = p
        sommedue += p * prix(n,e-o)
        #print o,e,p,prix(n,e-o),sommedue
    s = list(stops)
    s.sort()
    passagers = []
    sommepayee = 0
    for stop in s:
        #print
        #print stop
        ##print passagers
        if stop in departs:
            #print "ici"
            #print passagers
            passagers.append((stop,departs[stop]))
            #print passagers
        if stop in arrivees:
            #print "la"
            #print passagers
            descentes = arrivees[stop]
            while (descentes != 0):
                (dernierdepart,nombre) = passagers.pop()
                #print "pop"
                #print passagers
                if (nombre >= descentes):
                    #print "coucou"
                    reste = nombre - descentes
                    sommepayee += descentes * prix(n,stop-dernierdepart)
                    descentes = 0
                    if (reste != 0):
                        #print "append"
                        passagers.append((dernierdepart,reste))
                else:
                    #print "coucou2"
                    descentes -= nombre
                    sommepayee += nombre * prix(n,stop-dernierdepart)
            #print passagers
    if (len(passagers) == 0):
        #print "(%d,%d)" % (sommedue,sommepayee)
        print "Case #%d: %d" % (case,sommedue-sommepayee)
    else:
        #print "WAT"
        print passagers
