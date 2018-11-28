T = int(raw_input())


for i in xrange(T):
    l1 = int(raw_input())
    l1d = []
    for j in xrange(4):
        if (j + 1) == l1:
            l1d = [int(x) for x in raw_input().split()]
        else:
            raw_input()
    l2 = int(raw_input())
    l2d = []
    for j in xrange(4):
        if (j + 1) == l2:
            l2d = [int(x) for x in raw_input().split()]
        else:
            raw_input()

    count = 0
    val = 0
    for k,j in [(x,y) for x in l1d for y in l2d]:
        if k == j:
            count += 1
            val = k
    
    if count == 0:
        print "Case #%d: Volunteer cheated!"%(i+1,)
    elif count == 1:
        print "Case #%d: %d"%(i+1,val)
    else:
        print "Case #%d: Bad magician!"%(i+1,)
