T = int(raw_input())

def solve(X, R, C):
    """
    Can Richard block Gabriel with the piece selection?
    """
    if X == 1:
        return False

    # Not enough tiles
    if R * C < X:
        return True

    if (R * C) % X != 0:
        return True

    if X == 2:
        if (R * C) % 2 == 0:
            return False
        else:
            return True
    
    if X == 3:
        if R == 1 or C == 1:
            return True
        elif R == 3 or C == 3:
            return False
        elif R * C == 8:
            return True
        elif R * C == 4:
            return True
        else:
            print "MAYBE: %s, %s, %s" % (X, R, C)
            return False
    
    if X == 4:
        if R == 1 or C ==1:
            return True
        elif C * R == 4:
            return True
        elif C * R == 8:
            return True
        elif C * R == 12:
            return False
        elif C * R == 16:
            return False

        else:
            print "MAYBE: %s, %s, %s" % (X, R, C)
            return False

    print "UNKNOWN"



for t in xrange(1,T+1):
    (X, R, C) = [int(x) for x in raw_input().split()]
    print "Case #%s: %s" % (t, "RICHARD" if solve(X, R, C) else "GABRIEL") 
