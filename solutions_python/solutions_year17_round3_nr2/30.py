import sys

def build_gaps(activities):
    """
    activities: [ (start, end, who) ... ]  Sorted.
    Returns [ (length, preference) ... ] of the gaps.
    """
    gaps = []
    for i, act1 in enumerate(activities):
        if i == len(activities) - 1:
            act2 = (activities[0][0] + 1440, activities[0][1] + 1440, activities[0][2])
        else:
            act2 = activities[i+1]
        length = act2[0] - act1[1]
        assert length >= 0
        preference = act1[2] if act1[2] == act2[2] else None
        gaps.append((length, preference))
    return gaps


def calc_missing(activities, who):
    used = 0
    for act in activities:
        if act[2] == who:
            used += act[1] - act[0]
    assert used <= 720
    return 720 - used


def least_switches(activities):
    if len(activities) <= 1:
        return 2
    gaps = sorted(build_gaps(activities))
    missingC = calc_missing(activities, "C")
    missingJ = calc_missing(activities, "J")
    costs = []  # parallel to gaps
    for i, (gaplen, gappref) in enumerate(gaps):
        if gappref is None:
            costs.append(1)
        elif gappref == "C" and gaplen <= missingC:
            costs.append(0)
            missingC -= gaplen
        elif gappref == "J" and gaplen <= missingJ:
            costs.append(0)
            missingJ -= gaplen
        else:
            costs.append(2)
    return sum(costs)


if __name__ == "__main__":
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        AC, AJ = [int(part) for part in sys.stdin.readline().split()]
        activities = []
        for (who, count) in [("C", AC), ("J", AJ)]:
            for _ in xrange(count):
                start, end = [int(part) for part in sys.stdin.readline().split()]
                activities.append((start, end, who))
        activities.sort()
        least = least_switches(activities)
        print "Case #%d: %d" % (i+1, least)
