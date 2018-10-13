t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t+1):
    N, R, O, Y, G, B, V  = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    # R = R - G
    # O = O - B
    # Y = Y - V
    
    unicorns = [['R', R], ['Y', Y], ['B', B]]
    unicorns.sort(reverse=True, key= lambda x:x[1])
    # print unicorns
    if unicorns[0][1] <= N/2:
        # tmp = unicorns.values.sort(reverse=True)
        result = ''
        k = (unicorns[1][1] + unicorns[2][1]) - unicorns[0][1]
        result += (unicorns[0][0] + unicorns[1][0] + unicorns[2][0]) * k
        for j in range(3):
            unicorns[j][1] -= k
        result += (unicorns[0][0] + unicorns[1][0]) * unicorns[1][1]
        result += (unicorns[0][0] + unicorns[2][0]) * unicorns[2][1]
        
    else:
        result = 'IMPOSSIBLE'
    
    print "Case #{}: {}".format(i, result)
