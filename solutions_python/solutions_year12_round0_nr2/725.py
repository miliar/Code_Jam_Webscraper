c = int(raw_input())
for i in range(c):
    print "Case #" + str(i+1) + ":",
    line = raw_input();
    num = line.split()
    th = int(num[2])
    special = int(num[1])
    thUp = th*3 - 2
    thLow = th*3 - 4
    if thLow < 2:
        special = 0
    count = 0
    for s in num[3:]:
        if int(s) >= thUp:
            count = count + 1
        elif int(s) >= thLow and  special > 0:
            count = count + 1
            special = special - 1
    print count



