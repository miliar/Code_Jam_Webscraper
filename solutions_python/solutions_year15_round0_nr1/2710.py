
# GCJ 2015 Qual A jeremy.holman@gmail.com

T = int(raw_input())

for t in xrange(T):
    _, S = raw_input().split()
    S = map(int, S)
    answer = 0
    avail = 0
    for i in xrange(len(S)):
        avail += S[i]
        if avail > 0:
            avail -= 1
        else:
            answer += 1

    print "Case #%i: %i" % (t+1, answer)
    
