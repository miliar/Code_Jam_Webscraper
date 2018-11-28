#
"""
 brief:
"""
#
# qointe, 2014-04-12, qointe@yahoo.in
#

for i in xrange(int(raw_input().rstrip())):
    c, f, x = map(float, raw_input().rstrip().split())
    r = 2
    time = 0
    while True:
        if x/r < x/(r+f) + c/r:
            time += x/r
            break
        else:
            time += c/r
            r += f
    print "Case #{}: {}".format(i+1, time)
