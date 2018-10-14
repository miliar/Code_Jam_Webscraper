from itertools import groupby

def all_same_length(items):
    items = map(list, items)
    return all(len(x) == len(items[0]) for x in items)

def all_same(items):
    return all(x == items[0] for x in items)

def distance(a, b):
    return sum(abs(i - j) for i, j in zip(a, b))

T = int(raw_input())

for case in range(T):
    N = int(raw_input())
    strings = [raw_input() for i in range(N)]

    if not all_same(map(set, strings)):
        print "Case #{}: Fegla Won".format(case + 1)
        continue

    order = [k for k, g in groupby(strings[0])]
    bad = False
    for group in map(groupby, strings):
        if [k for k, g in group] != order:
            print "Case #{}: Fegla Won".format(case + 1)
            bad = True
            break # sorry for the horrible code had to fix quickly

    if bad:
        continue

    lengths = []
    for group in map(groupby, strings):
        lengths.append([len(list(g)) for k, g in group])

    dist = distance(lengths[0], lengths[1])
    print "Case #{}: {}".format(case + 1, dist)
