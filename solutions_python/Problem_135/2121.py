tc = input()
for tid in range(1, tc + 1):
    r1 = input()
    for i in range(4):
        line = raw_input()
        if i + 1 == r1:
            s1 = set(map(int, line.split()))
    r2 = input()
    for i in range(4):
        line = raw_input()
        if i + 1 == r2:
            s2 = set(map(int, line.split()))
    s = s1 & s2
    if len(s) == 1:
        ctrl = str(list(s)[0])
    elif len(s) > 1:
        ctrl = "Bad magician!"
    else:
        ctrl = "Volunteer cheated!"
    print "Case #" + str(tid) + ": " + ctrl
