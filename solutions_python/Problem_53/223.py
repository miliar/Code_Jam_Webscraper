#! /usr/bin/python
T =int(raw_input())
for case in xrange(1,T+1):
    N,K = map(int, raw_input().split())
    K = (K % (1 << N))
    if (K == ( (1<<N) -1)):
        print "Case #%d: ON" % (case, )
    else:
        print "Case #%d: OFF" % (case, )
