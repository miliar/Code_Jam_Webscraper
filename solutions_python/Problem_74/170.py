f = open("in.txt","r")
out = open("out.txt","w")
cases = int(f.readline())
for case in xrange(1,cases+1):
    line = f.readline().split()
    k = int(line[0])
    OT = 0
    BT = 0
    OP = 1
    BP = 1
    TT = 0
    for i in xrange(1, 2*k+1, 2):
        if line[i]=='O':
            newPos = int(line[i+1])
            if newPos!=OP:
                OT += abs(newPos-OP)+1
                OP = newPos
            else: OT+=1
            if OT<=TT:
                OT=TT+1
                TT+=1
            else:
                TT = OT
        elif line[i]=='B':
            newPos = int(line[i+1])
            if newPos!=BP:
                BT += abs(newPos-BP)+1
                BP = newPos
            else: BT+=1
            if BT<=TT:
                BT=TT+1
                TT+=1
            else:
                TT = BT
    out.write("Case #%d: %d\n" % (case,TT))