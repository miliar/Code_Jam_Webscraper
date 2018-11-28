# Created By: Bryce Besler

canDo   = "GABRIEL";
cantDo  = "RICHARD";

T = int(raw_input());
for t in xrange(T):
    line = str(raw_input()).split(' ');
    X = int(line[0]);
    R = int(line[1]);
    C = int(line[2]);

    passed=True;

    if (R*C) % X != 0:
        passed=False

    if X == 1:
        pass;
    elif X == 2:
        if (R + C < 3):
            passed=False;
    elif X == 3:
        if (R < 2 or C < 2):
            passed=False;
    elif X == 4:
        if (R < 4 or C < 3) and (R < 3 or C < 4):
            passed=False;

    # Print
    if passed:
        print "Case #{t}: {ans}".format(t=t+1, ans=canDo);
    else:
        print "Case #{t}: {ans}".format(t=t+1, ans=cantDo);
