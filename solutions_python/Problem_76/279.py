c = int(raw_input())
for case in range(1, c+1):
    n = int(raw_input())
    candy = map(int,raw_input().split())

    tot = reduce(int.__xor__, candy)
    if tot == 0:
        print "Case #%d: %d" % (case, sum(candy)-min(candy))
    else:
        print "Case #%d: NO" % case
