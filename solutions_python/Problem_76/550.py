import psyco


def add(x,y):
##    print "adding",x,y
    exp = total = 0
    while x > 0 and y > 0:
        temp = (x % 2 + y % 2) % 2
##        print x, y, temp
        total += temp * 2**exp
        x /= 2
        y /= 2
        exp += 1

    total += (x + y) * 2**exp
##    print "returning",total
##    print ""
    return total
    
f = open("input.txt")

numcases = int(f.readline())

for case in xrange(numcases):
    numcandies = int(f.readline())
    candies = f.readline().split(" ")

    for index in xrange(len(candies)):
        candies[index] = int(candies[index])

    total = 0
    for candy in candies:
        total = add(total,candy)

    if total == 0:
        print "Case #%d: %d" %(case + 1, sum(candies) - min(candies))
    else:
        print "Case #%d: NO" %(case + 1)
    
    
##    print "Case #%d: %s" %(case + 1, result)

f.close()
