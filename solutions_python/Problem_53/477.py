import sys
f = open(sys.argv[1])
counter = 1
for line in f:
    li = line.split()
    if len(li) is 1:
        counter = counter - 1
    else:
        if (1 + int(li[1],10)) % 2**int(li[0],10) is 0:
            print "Case #%d: ON" % (counter, )
        else:
            print "Case #%d: OFF" % (counter, )
    counter = counter + 1
