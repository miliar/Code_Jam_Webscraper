def get_set():
    group = int(raw_input())
    groups = []
    for i in range(4):
        groups.append(set(map(int, raw_input().split())))
    return groups[group-1]

cases = int(raw_input())

for case in range(1, cases+1):
    hypotheses = set.intersection(get_set(), get_set())
    if not hypotheses:
        print "Case #{0}: Volunteer cheated!".format(case)
    elif len(hypotheses) > 1:
        print "Case #{0}: Bad magician!".format(case)
    else:
        print "Case #{0}: {1}".format(case, hypotheses.pop())
