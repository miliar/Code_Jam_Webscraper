T = int(raw_input())

for case in range(T):

    D,N = map(int, raw_input().split())
    endTime = 0.0
    for n in range(N):
        k,s = map(int, raw_input().split())
        endTime = max(endTime, (D-k)/float(s))


    ret = D/endTime


    print "Case #{0}: {1}".format(case+1, ret)
