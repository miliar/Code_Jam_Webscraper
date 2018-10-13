T = input()
for t in range(0, T):
    ls = []
    fn = []
    g1 = input()
    for i in range(0, 4):
        line = map(int, raw_input().split())
        if (g1 - 1 == i):
            for o in line:
                ls.append(o)

    g2 = input()
    for i in range(0, 4):
        line = map(int, raw_input().split())
        if (g2 - 1 == i):
            for o in line:
                if (o in ls):
                    fn.append(o)

    if (len(fn) == 0):
        print "Case #" + str(t + 1) + ": Volunteer cheated!"
    elif (len(fn) == 1):
        print "Case #" + str(t + 1) + ": " + str(fn[0])
    else:
        print "Case #" + str(t + 1) + ": Bad magician!"
