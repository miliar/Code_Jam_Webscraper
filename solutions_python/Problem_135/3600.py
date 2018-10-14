
t = int(raw_input())
for i in xrange(t):
    a1 = int(raw_input()) - 1
    m1 = []
    for j in xrange(4):
        m1.append( map(int, raw_input().split()) )
    
    a2 = int(raw_input()) - 1
    m2 = []
    for j in xrange(4):
        m2.append( map(int, raw_input().split()) )

    #print m1[a1], m2[a2]
    s = set(m1[a1]).intersection(set(m2[a2]))  
    if len(s) == 1:
        res = s.pop()
    elif len(s) > 1:
        res = "Bad magician!"
    else:
        res = "Volunteer cheated!"
    print "Case #%s: %s" % (i+1, res)
