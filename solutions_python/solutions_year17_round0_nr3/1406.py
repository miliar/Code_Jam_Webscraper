#!/usr/bin/env python

def find_s(x):
    s1 = x/2
    s2 = x - s1 - 1
    return s1, s2

t = int(raw_input())
for i in xrange(1, t + 1):
    num_stalls, num_people = [int(s) for s in raw_input().split(" ")]
    min_space = 0
    max_space = num_stalls
    min_space_count = 0
    max_space_count = 1
    p = 0
    group = 1
    
    while True:
        if p + group >= num_people:
            if num_people - p <= max_space_count:
                s1, s2 = find_s(max_space)
            else:
                s1, s2 = find_s(min_space)
            break
        else:
            s1_max, s2_max = find_s(max_space)
            s1_min, s2_min = find_s(min_space)
            if min_space_count == 0:
                max_space = s1_max
                min_space = s2_max
                if max_space == min_space:
                    max_space_count *= 2
                else:
                    min_space_count = max_space_count
            else:
                l = [s1_max] * max_space_count
                l.extend([s2_max] * max_space_count)
                l.extend([s1_min] * min_space_count)
                l.extend([s2_min] * min_space_count)
                min_space = s2_min
                max_space = s1_max
                if min_space == max_space:
                    max_space_count = l.count(max_space)
                    min_space_count = 0
                else:
                    max_space_count = l.count(max_space)
                    min_space_count = l.count(min_space)
            p += group
            group *= 2
    
    print "Case #{}: {} {}".format(i, s1, s2)
