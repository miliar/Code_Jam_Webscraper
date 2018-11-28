import sys

# When does B catch up to F?
def intersect(mf, df, mb, db):
    if mb == mf:
        return float("inf")
    else:
        return ((db - df)/360.0)*(mf*mb)/(mb-mf)


T = int(sys.stdin.readline())
for i in range(T):
    N = int(sys.stdin.readline())
    assert N <= 2
    if N == 1:
        sys.stdin.readline() # eat line
        print "Case #%d: %d" % (i+1, 0)
        continue
    else:
        d1, h1, m1 = map(int, sys.stdin.readline().strip().split())
        d2, h2, m2 = map(int, sys.stdin.readline().strip().split())
        assert h1 == 1
        assert h2 == 1
        if d1 > d2:
            db, mb = d1, m1
            df, mf = d2, m2
        else:
            db, mb = d2, m2
            df, mf = d1, m1
        i1 = intersect(mf, df, mb, db-360)
        if i1 > 0:
            if (i1/float(mf))*360 + df > 360.0:
                print "Case #%d: %d" % (i+1, 0)
                continue
            else:
                print "Case #%d: %d" % (i+1, 1)
                continue
        else:
            i2 = intersect(mb, db, mf, df)
            # print "i2", i2
            assert i2 > 0
            if (i2/float(mb))*360 + db > 360.0:
                # print "a"
                print "Case #%d: %d" % (i+1, 0)
                continue
            else:
                dist = (i2/float(mb))*360 + db
                # front catches up twice
                i3 = intersect(mb, dist+360, mf, dist)
                # print "i3", i3
                if (i3/float(mb))*360 + dist > 360:
                    # print "b"
                    print "Case #%d: %d" % (i+1, 0)
                    continue
                else:
                    # print "c"
                    print "Case #%d: %d" % (i+1, 1)
                    continue

                
        
