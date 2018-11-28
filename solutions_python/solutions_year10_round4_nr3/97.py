import psyco
psyco.full()
for _ in xrange(1, input() + 1):
    solve_map = {}
    for R in xrange(input()):
        cord = [int(x) for x in raw_input().split()]
        for x in xrange(cord[0], cord[2] + 1):
            for y in xrange(cord[1], cord[3] + 1):
                solve_map[(x, y)] = 1
    time = 0
    while len(solve_map.keys()) != 0:
            new_map = {}
            for x, y in solve_map.keys():
                       if (x - 1, y) not in solve_map and (x, y - 1) not in solve_map:
                           pass
                       else:
                           new_map[(x, y)] = 1
                       if (x - 1, y + 1) in solve_map:
                           new_map[(x, y + 1)] = 1
                       if (x + 1, y - 1) in solve_map:
                           new_map[(x + 1, y)] = 1
            solve_map = new_map
            time += 1
    print  'Case #' + str(_) + ':', time
