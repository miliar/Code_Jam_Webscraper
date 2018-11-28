fi = open("B-small-attempt1.in", 'r')
fo = open("B-small-attempt1-out.out", 'w')

cache = {}

def minutes(plates):
    m = max(plates)
    # Base case: no more splits
    if m < 4:
        return m

    # check if cached. i think sorting is better than having duplicates
    tup = tuple(sorted(plates))

    if tup in cache:
        return cache[tup]

    # Otherwise recurse over possible splits of max.
    best = m
    # s = split amount
    for s in xrange(2, m/2+1):
        newplates = plates[:]
        newplates.append(s)
        newplates.append(m-s)
        newplates.remove(m)

        # +1 for split
        newminutes = minutes(newplates) + 1
        if newminutes < best:
            best = newminutes

    # cache it
    cache[tup] = best;

    return best

T = int(fi.readline())
for case in xrange(1, T + 1):
    D = int(fi.readline())
    plates = [int(x) for x in fi.readline().split()]
    fo.write("Case #{}: {}\n".format(case, minutes(plates)))

fi.close()
fo.close()
