from operator import xor

T = int(raw_input().strip())

for case in range(1,T+1):
    N = int(raw_input().strip())
    cc = map(int,raw_input().strip().split(' '))

    if reduce(xor,cc) != 0:
        print "Case #%d: NO" % (case)
    else:
        print "Case #%d: %d" % (case, sum(cc)-min(cc))

