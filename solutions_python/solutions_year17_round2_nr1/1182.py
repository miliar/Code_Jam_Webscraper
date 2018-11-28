from decimal import Decimal

for _ in xrange(1, input()+1):
    km, numhorses = map(Decimal, raw_input().split())
    time = max((km - distance) / speed for distance, speed in (map(Decimal, raw_input().split()) for h in xrange(int(numhorses))))
    print "Case #%d: %.6f" % (_, km / time)