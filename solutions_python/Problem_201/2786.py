import sys

def fill_stall(stalls):
    in_gap = False
    curr_gap_start = None
    max_gap_start = None
    max_gap_size = -1
    for i in range(len(stalls)):
        if stalls[i] == 0:
            if not in_gap:
               in_gap = True
               curr_gap_start = i
        else:
            if in_gap:
                in_gap = False
                gap_size = i - curr_gap_start
                if gap_size > max_gap_size:
                    max_gap_start = curr_gap_start
                    max_gap_size = gap_size
    if in_gap:
        gap_size = len(stalls) - curr_gap_start
        if gap_size > max_gap_size:
            max_gap_start = curr_gap_start
            max_gap_size = gap_size

    placement = None
    if max_gap_size % 2 == 1:
        placement = max_gap_start + max_gap_size / 2
        max = min = max_gap_size / 2
    else:
        placement = max_gap_start + max_gap_size / 2 - 1
        max = max_gap_size / 2
        min = max_gap_size / 2 - 1
        
    stalls[placement] = 1
    return placement, max, min

first = True
case = 0
for l in sys.stdin:
    l = l.rstrip()
    if first:
        first = False
        continue
    case += 1

    str_vals = l.split()
    n = int(str_vals[0])
    k = int(str_vals[1])
    stalls = [0] * n
    for i in range(k-1):
        fill_stall(stalls)
    placement, max, min = fill_stall(stalls)
    print "Case #" + str(case) + ": " + str(max) + " " + str(min)
