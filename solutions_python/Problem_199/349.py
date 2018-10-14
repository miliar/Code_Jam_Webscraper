t = int(raw_input())  # read a line with a single integer
for task in xrange(1, t + 1):
    params = raw_input().split(" ")
    cakes = list(params[0])
    l = int(params[1])

    flip = [0] * len(cakes)

    for i in range(0, len(cakes) - l + 1):
        test = 0
        for j in range(1, l):
            if i - j >= 0:
                test += flip[i - j]

        if cakes[i] == "-":
            test += 1

        flip[i] = test % 2

#        print "{}: {}".format(i, test)
#        print " ".join(cakes)
#        print " ".join([str(num) for num in flip])
#        print ""

    have_sol = True
    for i in range(len(cakes) - l + 1, len(cakes)):
        test = 0
        for j in range(1, l):
            if i - j >= 0:
                test += flip[i - j]
        if cakes[i] == "-":
            test += 1

        if test % 2 != 0:
            have_sol = False

    if have_sol:
        print "Case #{}: {}".format(task, flip.count(1))
    else:
        print "Case #{}: {}".format(task, "IMPOSSIBLE")



