lines = [ x for x in open("input.txt") ]
cases = int(lines.pop(0))
def fill_coaster(supply, rides, groups):
    index  = 0
    startIndex = 0
    length = len(groups)
    money  = 0
    for ride in range(rides):
        s = supply
        while True:
            group = groups[index]
            s -= group
            if s < 0:
                break
            money += group
            index  = (index + 1) % length
            if index == startIndex:
                break
        startIndex = index
    return money

for case in xrange(cases):
    r, k, n = [ int(x) for x in lines.pop(0).split() ]
    groups  = [ int(x) for x in lines.pop(0).split() ]
    money = fill_coaster(k, r, groups)
    print "Case #%i: %s" % (case + 1, money)