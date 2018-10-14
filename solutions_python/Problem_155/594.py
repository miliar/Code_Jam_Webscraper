def read_ints():
    ns = map(int,raw_input().split())
    return ns if len(ns) > 1 else ns[0]

for case in range(1,read_ints()+1):
    smax,ss = raw_input().split()
    smax = int(smax)
    ss = map(int,ss)
    friends = 0
    for i in range(1,len(ss)):
        friends += max(0,i - sum(ss[0:i]) - friends)
    print "Case #%d: %d" % (case,friends)


