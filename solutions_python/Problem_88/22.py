def is_com (grid, k, start_c, start_r):
       end_c = start_c + k - 1
       end_r = start_r + k - 1
       centre_c = (start_c + end_c)/2.0
       centre_r = (start_r + end_r)/2.0
       tot = [0, 0]
       for r in xrange (start_r, start_r+k):
              for c in xrange(start_c, start_c+k):
                     tot[0] += (r - centre_r) * grid[r][c]
                     tot[1] += (c - centre_c) * grid[r][c]
       tot[0] -= (start_r - centre_r) * grid[start_r][start_c]
       tot[1] -= (start_c - centre_c) * grid[start_r][start_c]
       tot[0] -= (start_r - centre_r) * grid[start_r][end_c]
       tot[1] -= (end_c - centre_c) * grid[start_r][end_c]
       tot[0] -= (end_r - centre_r) * grid[end_r][start_c]
       tot[1] -= (start_c - centre_c) * grid[end_r][start_c]
       tot[0] -= (end_r - centre_r) * grid[end_r][end_c]
       tot[1] -= (end_c - centre_c) * grid[end_r][end_c]
       return abs(tot[0]) < 1e-8 and abs(tot[1]) < 1e-8

T = input()
for t in xrange(T):
       max_k = -1
       R, C, D = map(int, raw_input().split())
       grid = [[D + int(x) for x in raw_input()] for r in xrange(R)]
       for k in xrange (3, min(C, R)+1):
              for start_c in xrange (C - k + 1):
                     for start_r in xrange (R - k + 1):
                            if is_com(grid, k, start_c, start_r):
                                   #print start_c, start_r, k
                                   max_k = k
       print "Case #%s: %s" % (t+1, "IMPOSSIBLE" if max_k == -1 else max_k)