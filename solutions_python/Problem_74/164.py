import sys

sys.stdin.readline() #skip number of tests
for d,line in enumerate(sys.stdin.readlines()):
    actions = [x.strip() for x in line.split(' ')][1:]
    count = 0
    B=O=1
    Bmoves = Omoves = 0
    for robot, num in zip(actions[::2], actions[1::2]):
        assert 1<=B<=100
        assert 1<=O<=100
        num = int(num)

        #print >>sys.stderr Bmoves,Omoves
        if robot == 'B':
            move = max(0, abs(num-B)-Omoves) +1
            B=num; Omoves=0
            count += move
            Bmoves += move
        else:
            move = max(0, abs(num-O)-Bmoves) +1
            O=num; Bmoves=0
            count += move
            Omoves += move

    assert count <= 10000
    print "Case #%d: %d" % (d+1, count)
