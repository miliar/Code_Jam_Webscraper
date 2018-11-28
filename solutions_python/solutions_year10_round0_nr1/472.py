for case in xrange(int(raw_input())):
    N, K = map(int, raw_input().split())
    t = 0
    for i in xrange(N):
        t += int(2**i)
    if t&K == t:
        answer = "ON"
    else:
        answer = "OFF"
    print "Case #%d:"%(case+1),answer
