import sys

# read int
casen = int(sys.stdin.readline().strip())

for i in range(1, casen+1):
    # read case
    v1, v2 = map(lambda x: x.strip(),
                        sys.stdin.readline().split(' ', 2))
    
    smax = int(v1)
    # read str
    audience = v2
    should_add = 0
    standing = 0
    for need in range(0, smax+1):
        # audience[need] people need `need` other people to stand
        # print audience[need]
        if audience[need] != 0:
            if need > standing:
                should_add += need - standing
                standing = need
            standing += int(audience[need]) - int('0')
    print "Case #%d: %d" % (i, should_add)
                       