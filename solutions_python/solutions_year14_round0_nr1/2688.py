t = int(raw_input())+1
for case in range(1,t):
    q1 = int(raw_input())-1
    g1 = []
    for r in range(4):
        g1.append(raw_input().split())
    p1 = g1[q1]                     
    q2 = int(raw_input())-1
    g2 = []
    for r in range(4):
        g2.append(raw_input().split())
    p2 = g2[q2]
    count = 0
    for i in p1:
        for j in p2:
            if i==j:
                count = count+1
                card = i
    print "Case #%s:" % case,
    if count==0:
        print "Volunteer cheated!"
    elif count==1:
        print card
    else:
        print "Bad magician!"
