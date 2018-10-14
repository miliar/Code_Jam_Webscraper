ncases = int(raw_input().strip())
for i in xrange(1,ncases+1):
    fields = raw_input().strip().split(' ')
    x = int(fields[0])
    width = int(fields[1])
    height = int(fields[2])
    if x>6 or (width*height)%x!=0:
        print "Case #{0}: RICHARD".format(i)
        continue
    if x<3:
        print "Case #{0}: GABRIEL".format(i)
        continue
    if width*height==x:
        print "Case #{0}: RICHARD".format(i)
        continue
    if x==3:
        if min(width,height)>1:
            print "Case #{0}: GABRIEL".format(i)
            continue
        else:
            print "Case #{0}: RICHARD".format(i)
            continue
    if min(width,height) > x:
        print "Case #{0}: GABRIEL".format(i)
        continue
    if x==4:
        if min(width,height)>2:
            print "Case #{0}: GABRIEL".format(i)
            continue
        else:
            print "Case #{0}: RICHARD".format(i)
            continue
    if min(width,height)<=x/2:
        print "Case #{0}: RICHARD".format(i)
    else:
        print "Case #{0}: GABRIEL".format(i)

