numTest = int(raw_input())
for i in range(numTest):
    (r, k, n) = [int(x) for x in raw_input().split(" ")]
    g = [int(x) for x in raw_input().split(" ")]
    # print "r%d k%d n%d" % (r, k, n)
    euros = 0
    front_idx = 0
    
    for j in range(0, r):
        num_board = 0
        while (num_board + g[front_idx] <= k) and (num_board + g[front_idx] <= sum(g)):
            num_board += g[front_idx]
            if front_idx == n - 1:
                front_idx = 0
            else:
                front_idx += 1
        euros += num_board
    print "Case #%d: %d" % (i + 1, euros)
            