def calculate(r, k, queue):
    money = 0
    run_cache = {}
    
    original_idx = 0
    run = 0
    while run < r:
        places_used = 0
        for idx, group_size in enumerate(queue):
            if places_used + group_size <= k:
                places_used += group_size
            else:
                break
        else:
            idx += 1
        
        groups_that_went = queue[0:idx]
        money_from_this_group = sum(groups_that_went)
        money += money_from_this_group
        del queue[0:idx]
        queue.extend(groups_that_went)
        run += 1
        
        run_cache[original_idx] = ((original_idx + idx) % len(queue), money_from_this_group)
        original_idx = (original_idx + idx) % len(queue)
        
        
        if original_idx in run_cache:
            # cycle detected
            cycle_money = 0
            cycle_step, cycle_step_money = run_cache[original_idx]
            cycle_money += cycle_step_money
            cycle_size = 1
            while cycle_step != original_idx:
                cycle_step, cycle_step_money = run_cache[cycle_step]
                cycle_money += cycle_step_money
                cycle_size += 1
            
            runs_left = r - run
            cycle_runs, runs_left = divmod(runs_left, cycle_size)
            money += cycle_runs * cycle_money
            
            run += cycle_runs*cycle_size
            run_cache.clear()
    
    return money


#print calculate(int(2e6), int(1e2), [33, 33, 33, 50] * 250, False)
#print calculate(int(2e6), int(1e2), [33, 33, 33, 50] * 250, True)
##print calculate(4, 6, [1, 4, 2, 1])
##print calculate(100, 10, [1])
##print calculate(5, 5,  [2, 4, 2, 3, 4, 2, 1, 2, 1, 3])

for case_number in xrange(int(raw_input())):
    r, k, n = map(int, raw_input().split())
    group_sizes = map(int, raw_input().split())
    
    result = calculate(r, k, group_sizes)
    print 'Case #%d: %d' % (case_number+1, result)