from math import ceil, floor

def readint(): return int(raw_input())
def readarray(x): return map(x, raw_input().split())

cases = readint()
for case in range(cases):

    stall_count, final_user = raw_input().split()
    stall_count = int(stall_count)
    final_user = int(final_user)

    checks_max = [long(stall_count)]
    checks_count = [1L]
    checks =[checks_max, checks_count]


    current_user = 0
    new_max = -1
    new_min = -1
    while 1:
        #print checks
        max_open = max(checks_max)
        max_open_index = checks_max.index(max_open)
        count_max = checks_count[max_open_index]
        current_user += count_max

        if max_open % 2 == 0:
            new_max = max_open/2
            new_min = max_open/2 - 1
        else:
            new_max = (max_open - 1) / 2
            new_min = (max_open - 1) / 2

        if final_user <= current_user:
            break

        checks_max.remove(max_open)
        del checks_count[max_open_index]
        if checks_max.count(new_max) > 0:
            checks_count[checks_max.index(new_max)] += count_max
        else:
            checks_max.append(new_max)
            checks_count.append(count_max)
        if checks_max.count(new_min) > 0:
            checks_count[checks_max.index(new_min)] += count_max
        else:
            checks_max.append(new_min)
            checks_count.append(count_max)

    print 'Case #%i:'%(case+1), new_max, new_min
