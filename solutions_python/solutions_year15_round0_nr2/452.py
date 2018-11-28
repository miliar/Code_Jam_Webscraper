data = open("input/problemb.txt")
nb_cases = int(data.readline())
for z in xrange(nb_cases):
    print "Case #%d:" % (z + 1),
    zzz = int(data.readline())
    pancakes = [int(x) for x in data.readline().split(" ")]

    max_minutes = max(pancakes)
    best_sol = max_minutes
    for nb_normal in xrange(1, max_minutes + 1):
        nb_special = 0
        for nb_pancakes in pancakes:
            if nb_pancakes > nb_normal:
                if nb_pancakes % nb_normal == 0:
                    nb_special += nb_pancakes / nb_normal - 1
                else:
                    nb_special += nb_pancakes / nb_normal

        if nb_special + nb_normal < best_sol:
            # print nb_special, nb_normal
            best_sol = nb_special + nb_normal
    print best_sol
