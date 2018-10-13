o = open("input.txt", "r").readlines()
count = 1
for i in o:
    ans = "Broken"
    if len(i.split()) == 3:
        N, PT, PG = [int(j) for j in i.split()]
        if N > 100:
            if PG == 0 or PG == 100:
                 if PG==PT:
                     ans = "Possible"
            else:
                ans = "Possible"
        else:
            for D in xrange(1, N+1):
                for wins in xrange(0, D+1):
                    if 100*wins == PT*D:
                        if PG == 0 or PG == 100:
                            if PG==PT:
                                ans = "Possible"
                        else:
                            ans = "Possible"
        print "Case #%d: %s" % (count, ans)
        count +=1
