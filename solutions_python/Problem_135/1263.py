ROWS = 4
results = []

num_of_cases = int(raw_input())
for case_num in xrange(num_of_cases):
    # Solve A
    solve_a = int(raw_input())
    for i in xrange(ROWS):
        num_list = raw_input()
        if i + 1 == solve_a:
            num_list_a = num_list.split()
    
    # Solve B
    solve_b = int(raw_input())
    for i in xrange(ROWS):
        num_list = raw_input()
        if i + 1 == solve_b:
            num_list_b = num_list.split()
    
    # Find Matches
    match_count = 0
    match_num = 0
    for num in num_list_a:
        if num in num_list_b:
            match_count += 1
            match_num = num
            
    # Set result
    if match_count == 1:
        results.append(match_num)
    elif match_count > 1:
        results.append('Bad magician!')
    else: #match_count == 0:
        results.append('Volunteer cheated!')
        
# Print results
for ind, res in enumerate(results):
    print 'Case #%d: %s' % (ind + 1, res)
