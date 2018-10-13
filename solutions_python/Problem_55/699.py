import sys
inputs_amnt = int(sys.stdin.readline())

for case_number in range(1,inputs_amnt+1):
    (runs,seats,groups) = ( int(x) for x in sys.stdin.readline().split(' ') )
    group_members_amnt = [ int(x) for x in sys.stdin.readline().split(' ') ]
    
    profit_nextgroupind_pairs = [] #consists of pairs (profit for a run starting with this group, index of group that will be first in the next run)
    i = -1
    for g in group_members_amnt:
        i += 1
        profit = group_members_amnt[i]
        nextgroupind = -1
        current_group_index = i
        no_more_groups_counter = groups
        while True:
            current_group_index += 1
            no_more_groups_counter -= 1
            current_group_index = current_group_index % (groups)
            next_profit = profit + group_members_amnt[current_group_index]
            if (next_profit > seats) or (no_more_groups_counter == 0):
                nextgroupind = current_group_index
                break
            else:
                profit += group_members_amnt[current_group_index]
        profit_nextgroupind_pairs.append( (profit, nextgroupind) )
    
    case_solution = 0
    i = 0
    for r in range(runs):
        (run_profit, i) = profit_nextgroupind_pairs[i]
        case_solution += run_profit
    sys.stdout.write('Case #%s: %s\n' % (case_number, case_solution))