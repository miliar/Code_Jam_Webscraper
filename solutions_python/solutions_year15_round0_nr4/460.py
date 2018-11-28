for i in xrange(input()):
    [X, R, C] = map(int, raw_input().split())
    if R*C % X != 0:
        print "Case #%d: %s" % (i+1, 'RICHARD') 
        continue
    if X == 1 or X == 2:
        print "Case #%d: %s" % (i+1, 'GABRIEL')
        continue
    if X == 3:
        if R == 1 or C == 1:
            print "Case #%d: %s" % (i+1, 'RICHARD') 
        else:
            print "Case #%d: %s" % (i+1, 'GABRIEL')
        continue
    if X == 4:
        if R < 3 or C < 3:
            print "Case #%d: %s" % (i+1, 'RICHARD') 
        else:
            print "Case #%d: %s" % (i+1, 'GABRIEL')
        continue




