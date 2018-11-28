cases = int(raw_input())

vowels = set('aeiou')

for case in range(cases):
    name, n = raw_input().split()
    n = int(n)
    # print("{} {}".format(name, n))

    seen = set()
    # print name, n
    for i in range(len(name) - n + 1):
        ss = set(name[i:i+n])
        if vowels.isdisjoint(ss):
            # print i, i+n, name[i:i+n]
            seen.add((i, i+n))
            for start in xrange(i+1):
                # print "startmid", start, i+n, name[start:i+n]
                seen.add((start, i+n))

                for end in xrange(i+n+1, len(name)+1):
                    # print "startmidend", start, end, name[start:end]
                    seen.add((start, end))


            # for end in xrange(i+n+1, len(name)+1):
            #     print "midend", i, end, name[i:end]
            #     seen.add((i, end))

    # print seen, len(seen)
    # print

    result = 0
    print "Case #{}: {}".format(case+1, len(seen))

