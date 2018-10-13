import sys

getline = lambda: sys.stdin.readline().replace("\n", "")
getlist = lambda: getline().split(" ")
getint = lambda: int(getline())
getints = lambda: map(int, getlist())

def possible(motes, A, addmotes):
    currentsize = A
    i = 0
    while i < len(motes):
        mote = motes[i]
        if mote < currentsize:
            currentsize += mote
        else:
            if addmotes > 0:
                # add a mote here
                currentsize += currentsize -1
                motes = motes[0:i] + [currentsize -1] + motes[i:]
                addmotes -=1
                assert motes[i+1] == mote
            else:
                return False
        i += 1
    return True

def operations(motes, A):
    # never more than length operations!
    length = len(motes)
    for ops in xrange(0, length+1):
        for delmotes in xrange(0, ops+1):
            testmotes = [m for m in motes[0:length-delmotes]]
            addmotes = ops - delmotes
            #print "ops, del, add = (%d, %d, %d)" % (ops, delmotes, addmotes)
            #print "testmotes = %s" % testmotes
            if possible(testmotes, A, addmotes):
                return ops
    return length



for t in xrange(1, 1+int(getline())):
    A, N = getints()
    motes = getints()
    assert len(motes) == N
    motes.sort()

    ops = operations(motes, A)
    assert ops <= N

    s = "%d" % ops
    print "Case #%d: %s" % (t, s)

