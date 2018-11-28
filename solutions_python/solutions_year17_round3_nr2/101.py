

def solve(c_times, j_times):

    time_remaining = 720
    other_person_remaining = 720

    for x,y in c_times:
        time_remaining -= (y-x)
    for x,y in j_times:
        other_person_remaining -= (y-x)

    c_times = [(x, y, True) for x,y in c_times]


    j_times = [(x, y, False) for x,y in j_times]
    c_times.extend(j_times)
    c_times.sort()

    # print c_times

    changes = 0
    gaps = []
    neutral_gaps = []
    other_gaps = []
    for i in xrange(1, len(c_times)):
        if c_times[i][2] and c_times[i-1][2]:
            # exists a gap
            time = c_times[i][0] - c_times[i-1][1]
            if time > 0:
                gaps.append(time)
        elif c_times[i][2] == c_times[i-1][2] and c_times[i-1][2] == False:
            # these gaps require 2 changes
            time = c_times[i][0] - c_times[i-1][1]
            if time > 0:
                other_gaps.append(time)
        else:
            time = c_times[i][0] - c_times[i-1][1]
            if time > 0:
                neutral_gaps.append(time)
            
        if c_times[i][2] != c_times[i-1][2]:
            changes += 1
    
    if len(c_times) > 1 or True:
        first = c_times[0]
        last = c_times[-1]
        if first[2] and last[2]:
            time = first[0] + 1440 - last[1]
            if time > 0:
                gaps.append(time)

        elif first[2] == last[2] and first[2] == False:
            time = first[0] + 1440 - last[1]
            if time > 0:
                other_gaps.append(time)

        else:
            time = first[0] + 1440 - last[1]
            if time > 0:
                neutral_gaps.append(time)

        if first[2] != last[2]:
            changes += 1


    

    # for any gap in gaps, + 2 changes
    # for any outer_gap removed, + 2 changes
    gaps.sort()
    other_gaps.sort(reverse=True)

    removed = []
    for g in gaps:
        if time_remaining >= g:
            time_remaining -= g
            removed.append(g)
    changes += (2 * (len(gaps) - len(removed)))

    if time_remaining > 0:
        for n in neutral_gaps:
            if time_remaining <= 0:
                break
            time_remaining -= n

    if time_remaining > 0:
        for o in other_gaps:
            if time_remaining <= 0:
                break
            time_remaining -= o
            changes += 2

    return changes


for i in xrange(input()):
    c, j = map(int, raw_input().split(' '))
    c_times = []
    j_times = []
    for q in xrange(c):
        c_times.append(map(int, raw_input().split(' ')))
    for q in xrange(j):
        j_times.append(map(int, raw_input().split(' ')))

    print "Case #%d: %d" % (i+1, solve(c_times, j_times))



