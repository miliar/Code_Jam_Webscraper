import sys

def lg(a) :
    sys.stderr.write(str(a)+"\n")

tn = int(sys.stdin.readline())
for testNr in range(1,tn+1) :
    print "Case #%d:" % testNr ,
    a = map(int,sys.stdin.readline().split())
    l, t, n, c = a[:4]
    a = a[4:]
    assert len(a)==c
    s = []
    su = 0
    for e in a :
	su += e
	s.append(su)
    bCycle = t / (2*su)
    bPosInC = t % (2*su)
    for i,e in enumerate(s) :
	if 2*e>= bPosInC :
	    diff = e-(bPosInC/2)
	    weAreAtMod = i
	    break

    nCycle = n/c
#    print "nCycle",nCycle,"su",su
    if n%c==0 :
	unBoostedTime = 2* (nCycle*su)
    else :
        unBoostedTime = 2* (nCycle*su + s[(n+c-1)%c])
#    print "unBoostedTime",unBoostedTime

    weAreAt = c*bCycle+weAreAtMod
#    print "weAreAt",weAreAt
#    print "diff",diff
    if weAreAt >=n :
	# no boost possible
	print unBoostedTime
	continue

    # tavolsag a mertekegysege
    boostPoss = []
    boostPoss.append(diff)
    for i in range(weAreAt+1,n) :
	boostPoss.append( a[i%c] )
#    print boostPoss
    boostPoss.sort()
    boostPoss.reverse()
    boostPoss = boostPoss[:l]
#    print boostPoss
#    print sum(boostPoss)
    totalBP = sum(boostPoss)
    print unBoostedTime-totalBP
    