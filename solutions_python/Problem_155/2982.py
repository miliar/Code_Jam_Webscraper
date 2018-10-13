import string, sys

input = file(sys.argv[1]).readline

def ovate(a):
    t = 0
    clapping = 0
    people = a.split()[1]
    for i in xrange(len(people) - 1):
        clapping += int(people[i])
        while i+1 > clapping:
            t += 1
            clapping += 1
    return t



for case in xrange(int(input())):
    print "Case #%d: %s" % (case+1,
                            ovate(input()))