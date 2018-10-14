for x in xrange(int(raw_input())):
    a=raw_input()
    a+=raw_input()
    a+=raw_input()
    a+=raw_input()
    b=raw_input()
    X=0
    O=0
    sig=0
    for frame in [a[0:4],a[4:8],a[8:12],a[12:],a[0]+a[4]+a[8]+a[12],a[1]+a[5]+a[9]+a[13],a[2]+a[6]+a[10]+a[14],a[3]+a[7]+a[11]+a[15],a[0]+a[5]+a[10]+a[15],a[3]+a[6]+a[9]+a[12]]:
        if frame=="OOOO" or frame=="OOOT" or frame=="OOTO" or frame=="OTOO" or frame=="TOOO":
            O+=1
            break
        elif frame=="XXXX" or frame=="XXXT" or frame=="XXTX" or frame=="XTXX" or frame=="TXXX":
            X+=1
            break
    if "." in a:
        sig+=1
    if O==1:
        print "Case #%d: O won" % (x+1)
    elif X==1:
        print "Case #%d: X won" % (x+1)
    elif sig==1:
        print "Case #%d: Game has not completed" % (x+1)
    else:
        print "Case #%d: Draw" % (x+1)