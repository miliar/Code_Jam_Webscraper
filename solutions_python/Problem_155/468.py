import sys



def run(idx):
    line = sys.stdin.readline()
    arr = line.split(' ')
    Smax = int(arr[0])
    digs = arr[1]

    cur = 0
    invitenum = 0
    for i in xrange(0, Smax +1):
        s = int(digs[i])
        if i > cur:
            invitenum = invitenum + i - cur
            cur = i

        cur = cur + s
        #print "idx=",i," ",cur

    res = "Case #%d: %d" % (idx, invitenum)
    print res

num = int(sys.stdin.readline())
for i in xrange(1, num+1):
    #print "=========", i
    run(i)


