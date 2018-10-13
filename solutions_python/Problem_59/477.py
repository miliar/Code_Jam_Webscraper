for x in xrange( input() ):
    N,M = (int(i) for i in raw_input().split())
    tree = dict()

    # parse given paths
    for i in xrange ( N ):
        path = raw_input()
        elements = path.split("/")[1:]
        construct = ""
        for e in elements:
            construct += e
            tree[construct] = 1

    # count the mkdirs
    count = 0
    for i in xrange ( M ):
        path = raw_input()
        elements = path.split("/")[1:]
        construct = ""
        for e in elements:
            construct += e
            try:
                foo = tree[construct]
            except KeyError:
                count += 1
                tree[construct] = 1

    print "Case #%d:" % (x+1) , count

