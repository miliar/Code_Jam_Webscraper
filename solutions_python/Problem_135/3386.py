def getArrange():
    row = input()
    arrange = []
    for j in range(4):
        arrange.append(set(raw_input().split()))
    return arrange[row-1]

t = input()
for i in range(1, t+1):
    output = "Volunteer cheated!"
    a1 = getArrange()
    a2 = getArrange()
    s = a1 & a2
    if len(s) == 1:
        output = s.pop()
    elif len(s) > 1:
        output = "Bad magician!"


    print "Case #%d: %s" % (i, output)