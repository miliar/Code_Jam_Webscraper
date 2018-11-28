#!/usr/bin/env python
from collections import deque

def solve_test(num_runs, coaster_length, num_groups, groups):
    #print groups
    
    money_made = 0
    # Do one run
    for i in range(num_runs):
        #print "Run: %s" % i
        # Reset for this run
        space_left = coaster_length
        stop = False
        run_group = []
        while(stop == False):
            #print groups
            if len(groups):
                group = groups.popleft()
                # This group can fit
                if group <= space_left:
                    money_made = money_made + group
                    space_left = space_left - group
                    run_group.append(group)
                    #print "Using: %s Groups: %s Money: %s" % (group, groups, money_made)
                
                    #print money_made
                else:
                    # Put it back
                    groups.appendleft(group)
                    stop = True
            else:
                stop = True
                
        groups.extend(run_group)
            
        
    return money_made

    
if __name__ == "__main__":
    # Parse the file, and send in the details
    import fileinput
    it = fileinput.input()
    tests = int(it.next().strip())
    for x in range(1, tests+1):
        #print "Case #%s" % (x)
        num_runs, coaster_length, num_groups = map(int, it.next().split())
        groups = deque(map(int, it.next().split()))
        
        answer = solve_test(num_runs, coaster_length, num_groups, groups)
        
        print "Case #%s: %s" % (x, answer)