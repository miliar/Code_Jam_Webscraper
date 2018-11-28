import sys

inp = open('A-small-3.in','r')
tn = int( inp.readline().rstrip() )
for cc in xrange(1,tn+1):
    ret = "Broken"
    
    N, PD, PG = map( int, inp.readline().rstrip().split() )
    for D in xrange(1,N+1):
        if D * PD % 100 == 0:
            WD = D * PD / 100
            for G in xrange(0,1001):
                for WG in xrange(0,G+1):
                    GG = D + G
                    WGG = WG + WD
                    if WGG > GG: continue
                    if WGG * 100 == GG * PG:
                        ret = "Possible"
                        break
                if ret == "Possible":
                    break
            if ret == "Possible":
                break
        if ret == "Possible":
            break
    print "Case #%d: %s"%(cc,ret)
