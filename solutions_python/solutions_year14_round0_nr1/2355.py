t = int(raw_input())
for i in range(t):
    r1 = int(raw_input())
    for k in range(4):
        s = raw_input()
        if k == r1 - 1:
            l1 = s.split()
    
    r2 = int(raw_input())
    for k in range(4):
        s = raw_input()
        if k == r2 - 1:
            l2 = s.split()
    
    l3 = [it for it in l2 if it in l1]
    if len(l3) == 0:
        print "Case #%i: Volunteer cheated!"%(i+1)
    elif len(l3) == 1:
        print "Case #%i:"%(i+1), l3[0]
    else:
        print "Case #%i: Bad magician!"%(i+1)
