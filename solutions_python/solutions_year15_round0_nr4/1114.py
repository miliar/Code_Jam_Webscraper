import sys

f = open(sys.argv[1])
f.readline()

t = 1
for l in f:
    x,r,c = [int(y) for y in l.split()]

    output = "GABRIEL"

    if x == 2 and (r*c)%2:
        output = "RICHARD"

    if x == 3:
        if max(r,c)<3 or min(r,c)<2 or (r*c)%3:
            output = "RICHARD"
    
    if x == 4:
        if max(r,c)<4 or min(r,c)<3 or (r*c)%4:
            output = "RICHARD"

    print "Case #{}: {}".format(t,output)
    t += 1
