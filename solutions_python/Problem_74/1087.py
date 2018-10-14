def calc(inp):
    btime = 0
    otime = 0
    bpos = 1
    opos = 1
    curtime = 0
    inp = inp.split()
    arr1 = inp[1::2]
    arr2 = map(int, inp[2::2])
    arr = map(lambda i: (arr1[i], arr2[i]), xrange(len(arr1)))

    for item in arr:
        if item[0] == 'O':
            otime += abs(opos - item[1])
            if curtime > otime:
                otime = curtime
            else:
                curtime = otime
            otime += 1
            curtime += 1
            opos = item[1]
        else:
            btime += abs(bpos - item[1])
            if curtime > btime:
                btime = curtime
            else:
                curtime = btime
            btime += 1
            curtime += 1
            bpos = item[1]
    print curtime

n = int(raw_input())
for t in xrange(n):
    inp = raw_input()
    print "Case #%d:" % (t+1),
    calc(inp)
