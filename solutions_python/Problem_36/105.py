#!/usr/bin/python

N=input()

target = 'welcome to code jam' # 19 chars

for test_nr in xrange(N):
    test_case = raw_input()
    v0 = [1]+[0]*len(target)
    v1 = [1]+[0]*len(target)
    for c in test_case:
        for i in range(len(target)):
            if target[i] == c:
                v1[i+1] = v0[i]+v0[i+1]
        v0=v1

    print "Case #%d: %04d"%(test_nr+1, v0[19]%10000)



