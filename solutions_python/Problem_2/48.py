#! /usr/bin/env python

def get_lines( lines, pos ):
    turn = int( lines[pos] )
    pos = pos + 1
    nA2B, nB2A = [ int(e) for e in lines[pos].split() ]
    pos = pos + 1
    A2B = lines[ pos:pos+nA2B ]
    pos = pos+nA2B
    B2A = lines[ pos:pos+nB2A ]
    pos = pos + nB2A
    return [ turn, nA2B, nB2A, A2B, B2A, pos ]

def train_needed( turn, nA2B, nB2A, A2B, B2A ):
    Time_A2B = [ time2minute(turn,e) for e in A2B ]
    Time_B2A = [ time2minute(turn,e) for e in B2A ]
    Time_A2B.sort()
    Time_B2A.sort()
    t = 0
    side = 3    # 1 -- A, 2 -- B, 3 -- unknown
    Atrain = 0
    Btrain = 0
    found = -1
    v = True
    v = False
    while len( Time_A2B ) + len( Time_B2A ) > 0:
        if found != None:
            if v: print Time_A2B, "---", Time_B2A
        if side == 3:
            if len( Time_A2B ) > 0 and len( Time_B2A ) > 0:
                if Time_A2B[0] <= Time_B2A[0]:
                    side = 1
                else:
                    side = 2
            elif len( Time_A2B ) == 0:
                side = 2
            elif len( Time_B2A ) == 0:
                side = 1
            else:
                raise()
            if side == 1:
                Atrain = Atrain + 1
                if v: print "send A"
            elif side == 2:
                Btrain = Btrain + 1
                if v: print "send B"
            else:
                raise()
        if side == 1:
            found = trip4me( Time_A2B, t )
        elif side == 2:
            found = trip4me( Time_B2A, t )
        else:
            raise()
        if found == None:
            # send a new train
            t = 0
            side = 3
        else:
            d, t = found
            side = 3 - side
    return Atrain, Btrain

def trip4me( Time, t ):
    i = 0
    found = None
    for d,a in Time:
        #print t,d,a
        if t <= d:
            found = Time.pop(i)
            break
        i = i + 1
    return found

def time2minute( turn, timetable ):
    """turn time add to arrival time"""
    Depart,   Arrival = timetable.split()
    hDepart,  mDepart = [ int(e) for e in Depart.split(":") ]
    hArrival, mArrival = [ int(e) for e in Arrival.split(":") ]
    tDepart  = hDepart*60 + mDepart
    tArrival = hArrival*60 + mArrival + turn
    return [ tDepart, tArrival ]

def train2way( turn, nA2B, nB2A, A2B, B2A ):
    Time_A2B = [ time2minute(turn,e) for e in A2B ]
    Time_B2A = [ time2minute(turn,e) for e in B2A ]
    #for d,a in Time_A2B:
    #    ttd = "%02i:%02i" % divmod( d,60 )
    #    tta = "%02i:%02i" % divmod( a,60 )
    #    print ttd, tta
    #for d,a in Time_B2A:
    #    ttd = "%02i:%02i" % divmod( d,60 )
    #    tta = "%02i:%02i" % divmod( a,60 )
    #    print ttd, tta
    Time_A2B.sort()
    Time_B2A.sort()
    A2Bdep = []
    A2Barv = []
    for d,a in Time_A2B:
        A2Bdep.append( d )
        A2Barv.append( a )
    B2Adep = []
    B2Aarv = []
    for d,a in Time_B2A:
        B2Adep.append( d )
        B2Aarv.append( a )
    t = 0
    Atrain = 0
    Btrain = 0
    ato = 0
    bto = 0
    Apool = 0
    Bpool = 0
    apo = 0
    bpo = 0
    # verbose
    v = True
    v = False
    for t in range( 1440 ):
        tt = "%02i:%02i" % divmod( t,60 )
        if t in A2Barv:
            n = A2Barv.count(t)
            Bpool = Bpool + n
            if v:
                print tt,
                print "ArB: Apo:%i->%i; Bpo:%i->%i; Atr:%i->%i; Btr:%i->%i" % \
                               (apo,Apool,  bpo,Bpool, ato,Atrain, bto,Btrain)
            bpo = Bpool
        if t in B2Aarv:
            n = B2Aarv.count(t)
            Apool = Apool + n
            if v:
                print tt,
                print "BrA: Apo:%i->%i; Bpo:%i->%i; Atr:%i->%i; Btr:%i->%i" % \
                               (apo,Apool,  bpo,Bpool, ato,Atrain, bto,Btrain)
            apo = Apool
        if t in A2Bdep:
            need = A2Bdep.count(t)
            Apool = Apool - need
            if Apool < 0:
                Atrain = Atrain + abs( Apool )
                Apool  = 0
            if v:
                print tt,
                print "AdA: Apo:%i->%i; Bpo:%i->%i; Atr:%i->%i; Btr:%i->%i" % \
                               (apo,Apool,  bpo,Bpool, ato,Atrain, bto,Btrain)
            ato = Atrain
            apo = Apool
        if t in B2Adep:
            need = B2Adep.count(t)
            Bpool = Bpool - need
            if Bpool < 0:
                Btrain = Btrain + abs( Bpool )
                Bpool  = 0
            if v:
                print tt,
                print "BdB: Apo:%i->%i; Bpo:%i->%i; Atr:%i->%i; Btr:%i->%i" % \
                               (apo,Apool,  bpo,Bpool, ato,Atrain, bto,Btrain)
            bto = Btrain
            bpo = Bpool
    #print Apool, Bpool
    return [ Atrain, Btrain ]

def main():
    import sys
    argv = sys.argv
    fin = argv[1]
    f = file( fin )
    ls = f.readlines()
    ls = [ s.strip() for s in ls ]
    f.close()
    nc = int( ls[0] )
    pos = 1
    for i in range( nc ):
        turn, nA2B, nB2A, A2B, B2A, pos = get_lines( ls, pos )
        #print turn, nA2B, nB2A, A2B, B2A, pos
        method = 1
        if method == 1:
            # list remove method
            Atrain, Btrain = train_needed( turn, nA2B, nB2A, A2B, B2A )
            print "Case #%i: %i %i" %( i+1, Atrain, Btrain )
        elif method == 2:
            # time scan method
            Atrain, Btrain = train2way( turn, nA2B, nB2A, A2B, B2A )
            print "Case #%i: %i %i" %( i+1, Atrain, Btrain )
        else:
            print "method %s not avaliable" % method
            pass
    return

if __name__ == "__main__":
    main()

