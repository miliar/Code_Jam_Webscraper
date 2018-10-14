import sys

input = sys.stdin


def process(data):
    pb = 1 # position of B
    po = 1 # position of O
    tb = 0 # time for move B
    to = 0 # time for move O
    rprev = '' # move switch
    t = 0

    for x in data:
        r, d = (x[0], int(x[1:]))
        if r == 'O':
            do = abs(po - d)
            if to > do:
                to = to - do
                do = 0
            else:
                do = do - to
                to = 0
            t += do
            po = d
            to = 0
            t += 1
            tb += do + 1
        if r == 'B':
            db = abs(pb - d)
            if tb > db:
                tb = tb - db
                db = 0
            else:
                db = db - tb
                tb = 0
            t += db
            pb = d
            tb = 0
            t += 1
            to += db + 1
        # print '--', t, to, tb
    return t


T=int(input.readline())
for i in xrange(1,T+1):
    data = input.readline()
    data = data.split()[1:]
    data = ['%s%s' % (data[x], data[x+1]) for x in range(0, len(data),2)]
    # print data
    res = process(data)
    print "Case #%s: %s" % (i, res)

