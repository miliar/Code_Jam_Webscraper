# -*- coding: utf-8 -*-
import sys
fin = sys.stdin
N = int(fin.readline())
for case in range(1,N+1):
    r, k, n = map(int, fin.readline().split())
    g = map(int, fin.readline().split())
    next_group = 0
    total = 0
    total_at = {}
    current_ride = 0
    while current_ride < r:
        current = 0
        group_count = 0
        while current + g[next_group] <= k and group_count < n:
            group_count += 1
            current += g[next_group]
            next_group = (next_group + 1) % n
        total += current
        if next_group in total_at:
            tdiff = total - total_at[next_group][0]
            rdiff = current_ride - total_at[next_group][1]
            repetitions = (r - current_ride - 1) / rdiff
            total += repetitions * tdiff
            current_ride += repetitions * rdiff
            
        else:
            total_at[next_group] = (total, current_ride)
            
        current_ride += 1
    
    
    print "Case #%d: %s" % (case, total)
