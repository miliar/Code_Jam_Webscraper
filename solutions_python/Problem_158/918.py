t = int(raw_input())
for tt in range(t) :
    print "Case #" + str(tt+1) + ":",
    x,r,c = [int(i) for i in raw_input().split()]
    if x == 1 :
        print "GABRIEL"
    elif x == 2 :
        if r*c < 2 or (r*c)%2 == 1 :
            print "RICHARD"
        else :
            print "GABRIEL"
    elif x == 3 :
        if r*c <= 3 or (r*c)%3 != 0 :
            print "RICHARD"
        else :
            print "GABRIEL"
    elif x == 4 :
        if r*c <= 4 or (r*c)%4 != 0 or (r*c) == 8 :
            print "RICHARD"
        else :
            print "GABRIEL"