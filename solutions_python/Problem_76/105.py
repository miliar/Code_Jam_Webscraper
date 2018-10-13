import operator, functools

T = int(raw_input())

for case in xrange(1, T+1):
    raw_input()
    numbers = map(int, raw_input().split())

    xor = functools.reduce(operator.xor, numbers, 0)

    if xor != 0:
        print "Case #%d: NO" % case
    else:
        print "Case #%d: %d" % (case, sum(numbers)-min(numbers))

