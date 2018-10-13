#encoding: utf-8

debug = False

# File reading
input = open('B-small-attempt0.in')

# Counting test cases
testn = int(input.readline())
tc = 0

# Utilities

# For each test case
while(tc < testn):
    # Process instructions
    t = input.readline().strip().split(' ')
    if debug:
        print t
    combine = {}
    opposed = []
    C = int(t[0])
    del t[0]
    for i in xrange(C):
        combine[t[i][:-1]] = t[i][-1]
        combine[t[i][:-1][::-1]] = t[i][-1]
        del t[i]

    D = int(t[0])
    del t[0]
    for i in xrange(D):
        opposed.append(t[i])
        opposed.append(t[i][::-1])
        del t[i]

    invoke = t[-1]

    if debug:
        print combine
        print opposed
        print invoke

    # Simulate process

    el = []
    for e in invoke:
        if len(el) > 0 and (el[-1] + e) in combine.keys() :
            el = el[:-1] + [combine[el[-1] + e]]
        else :
            el.append(e)
        for o in opposed:
            if o[0] == el[-1] and o[1] in el:
                el = []
                break

    # Print result
    print "Case #%d: %s" % (tc + 1, '[' + ', '.join(el) + ']')
    tc += 1
