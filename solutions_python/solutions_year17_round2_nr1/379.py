T = input()
for test in xrange(1, T+1):
    D, N = map(int, raw_input().split())
    horses = [map(int, raw_input().split()) for x in xrange(N)]
    maxTime = 0
    for pos, speed in horses:
        horseTime = (D-pos)/float(speed)
        maxTime = max([maxTime, horseTime])
    print "Case #%d: %.6f"%(test, D/maxTime)
