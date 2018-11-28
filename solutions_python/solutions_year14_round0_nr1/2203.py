T = int(raw_input())
for t in range(T):
    print "Case #{0}:".format(t+1),
    f = int(raw_input())
    b1, b2 = [], []
    for i in range(4):
        b1.append([int(j) for j in raw_input().split()])
    r1 = set(b1[f-1])
    s = int(raw_input())
    for i in range(4):
        b2.append([int(j) for j in raw_input().split()])
    r2 = set(b2[s-1])
    r = r1 & r2
    if len(r) > 1:
        print "Bad magician!"
    elif not r:
        print "Volunteer cheated!"
    else:
        print list(r)[0]