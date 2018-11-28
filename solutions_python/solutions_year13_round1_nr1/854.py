for TC in range(1, input()+1):
    r, t = map(int, raw_input().split())
    area = 0
    rings = 0
    next = 2*(n+1)-1
    while True:
        if area+next > t:
            break
        area += next
        next += 4
        rings += 1
    print "Case #%d: %d" % (TC, rings)