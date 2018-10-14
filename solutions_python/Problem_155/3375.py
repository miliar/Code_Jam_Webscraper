num_cases = int(raw_input())

for i in xrange(1,num_cases+1):
    smax, people = raw_input().split()
    count = 0;
    extra = 0
    for k, s in enumerate(people):
        if int(s) and count + extra < k:
            extra += k - (count + extra)
        count += int(s)

    print "Case #%d: %d" % (i, extra)

