t = int(raw_input())
    
for case in range(t):
    a = int(raw_input())
    for i in range(1,a):
        raw_input()
    row1 = set(int(x) for x in raw_input().split())
    for i in range(4-a):
        raw_input()
    a = int(raw_input())
    for i in range(1,a):
        raw_input()
    row2 = set(int(x) for x in raw_input().split())
    interx = row1.intersection(row2)
    l = len(interx)
    if l == 0:
        print "Case #" + str(case + 1) + ": Volunteer cheated!"
    elif l == 1:
        print "Case #" + str(case + 1) + ": " + str(interx.pop())
    else:
        print "Case #" + str(case + 1) + ": Bad magician!"
        #print str(l)
    for i in range(4-a):
        raw_input()    
