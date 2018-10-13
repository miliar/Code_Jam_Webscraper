hints = {}

def get_max_min(stalls, people):
    if stalls == people:
        return 0, 0
    if (stalls, people) in hints:
        return hints[(stalls, people)]
    gap_counts = {stalls: 1}
    for person in xrange(people):
        gaps = sorted(gap_counts.keys())
        biggest_gap = gaps[-1]
        gap_counts[biggest_gap] -= 1
        if gap_counts[biggest_gap] == 0:
            del gap_counts[biggest_gap]
        room_left = biggest_gap - 1
        min_gap_size = room_left / 2
        max_gap_size = room_left - min_gap_size
        for gap_size in min_gap_size, max_gap_size:
            if gap_size not in gap_counts:
                gap_counts[gap_size] = 0
            gap_counts[gap_size] += 1
    return max_gap_size, min_gap_size


for case in xrange(1, int(raw_input()) + 1):
    print "Case #%s: " % case,
    stalls, people = map(int, raw_input().split(" "))
    mx, mn = get_max_min(stalls, people)
    hints[(stalls, people)] = mx, mn
    print mx, mn
