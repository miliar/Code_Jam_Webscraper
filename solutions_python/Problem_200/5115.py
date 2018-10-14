t = int(raw_input())
for j in xrange(1, t+1):
    a = int(raw_input())
    x = False
    while x == False:
        y = False
        if a < 10:
            print "Case #%d:" % j, a
            break
        b = 0
        for i in xrange(len(str(a))-1):
            if str(a)[b] > str(a)[b+1]:
                break
            b += 1
            if i == len(str(a))-2:
                print "Case #%d:" % j, a
                y = True
        if y == True:
            break
        a -= 1
