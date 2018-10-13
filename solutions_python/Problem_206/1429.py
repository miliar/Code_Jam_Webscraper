T = int(raw_input().strip())

for i in xrange(T):
    D, N = [int(s) for s in raw_input().split(" ")]
    time_list = []
    temp_time = -1
    #print "D: {}, N: {}".format(D, N)
    for j in xrange(N):
        K, S = [int(s) for s in raw_input().split(" ")]
        temp = float(float(D - K) / S)
        if temp > temp_time:
            temp_time = temp
        #time_list.append(float(float(D - K) / S))
    #print time_list
    print "Case #{}: {}".format(i + 1, float(D / temp_time))
