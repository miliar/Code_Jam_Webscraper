t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    R, C = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case

    rows = []
    for j in range(R):
        rows.append(list(raw_input().strip()))
    
    for row in rows:
        last_a = None
        for j,a in enumerate(row):
            if a == '?' and last_a and last_a != '?':
                row[j] = last_a
            else:
                last_a = a
        
        last_a = None
        for j,a in enumerate(row[::-1]):
            if a == '?' and last_a and last_a != '?':
                row[-1-j] = last_a
            else:
                last_a = a

    # for j in range(C):
        # last_a = None
        # for k in range(R):
            # if a == '?' and last_a and last_a != '?':
                # row[j] = last_a
            # else:
                # last_a = a
    if R > 1: 
        for j, row in enumerate(rows):
            if '?' in row and j > 0:
                rows[j] = rows[j-1]

        for j, row in enumerate(rows[::-1]):
            if '?' in row:
                rows[-1-j] = rows[-1-j+1]
            

    # print "Case #{}: {} {}".format(i, n + m, n * m)
    print 'Case #{}:'.format(i)
    for j in range(R):
        print ''.join(rows[j])


