from math import pi

for t in xrange(1, input() + 1):
    n, stacksize = map(int, raw_input().split())
    cakes = [map(int, raw_input().split()) for c in xrange(n)]
    cakes.sort(reverse=True)
    bestarea = 0
    bestcakes = cakes[n - stacksize + 1:]
    bestcakes.sort(reverse=True, key=lambda cake: cake[0] * cake[1])
    #print cakes
    #print bestcakes
    for firstcake in xrange(n - stacksize, -1, -1):
        area = (cakes[firstcake][0] ** 2) + cakes[firstcake][1] * cakes[firstcake][0] * 2
        area += 2 * sum(cake[0] * cake[1] for cake in bestcakes)
        area *= pi
        bestarea = max(area, bestarea)
        bestcakes.append(cakes[firstcake])
        bestcakes.sort(reverse=True, key=lambda cake: cake[0] * cake[1])
        bestcakes.pop()
    print "Case #%d:" % t, bestarea