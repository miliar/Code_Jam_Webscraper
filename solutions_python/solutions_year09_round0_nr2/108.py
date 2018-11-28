def BFS(geomark, geoflow, start, startletter):
    start_h, start_w=start
    if not (start_h, start_w) in geomark:
        geomark[(start_h, start_w)]=startletter
        for to in geoflow[(start_h, start_w)]:
            if not (to[0], to[1]) in geomark:
                BFS(geomark, geoflow, (to[0], to[1]), startletter)

totalcase=int(raw_input())

U,L,R,S,SINK=(-1,0),(0,-1),(0,1),(1,0),(0,0)
DIRE=U,L,R,S,SINK

for casenum in xrange(totalcase):
    h,w=[int(e) for e in raw_input().split()]
    geo={}
    for hi in xrange(h):
        row=[int(e) for e in raw_input().split()][:w]
        for wi in xrange(w):
            geo[(hi, wi)]=row[wi]
    for hi in xrange(h):
        geo[(hi,-1)]=100000
        geo[(hi,w)]=100000
    for wi in xrange(w):
        geo[(-1,wi)]=100000
        geo[(h,wi)]=100000

    geoflow={}
    for hi in xrange(h):
        for wi in xrange(w):
            geoflow[(hi,wi)]=[]
    for hi in xrange(h):
        for wi in xrange(w):
            ulrs=[geo[(hi-1,wi)], geo[(hi,wi-1)], geo[(hi,wi+1)], geo[(hi+1,wi)]]
            lowest=min(ulrs)
            if lowest>=geo[(hi,wi)]:
                continue
            else:
                dire=DIRE[ulrs.index(lowest)]
                geoflow[(hi,wi)].append((hi+dire[0], wi+dire[1]))
                geoflow[(hi+dire[0], wi+dire[1])].append((hi,wi))

    geomark={}
    H,W=h,w
    startletter='a'
    for h in xrange(H):
        for w in xrange(W):
            if not (h,w) in geomark:
                BFS(geomark, geoflow,(h,w), startletter)
                startletter=chr(ord(startletter)+1)
            else:
                continue

    print "Case #%d:" % (casenum+1)
    for h in xrange(H):
        print " ".join([geomark[(h,w)] for w in xrange(W)])
