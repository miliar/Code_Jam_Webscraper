

def testSnapper(num_snappers, snaps):
    binary = bin(snaps)
    s = "%s" % (binary)
    s = s[-num_snappers:]
    #print s
    if s.count("1") == num_snappers:
        return True
    return False

for case in xrange(input()):
    N,K = map(int, raw_input().split())

    res = testSnapper(N, K)

    if res:
        print "Case #%i: ON" % (case+1)
    else:
        print "Case #%i: OFF" % (case+1)

