t = int(raw_input())  # read a line with a single integer

import numpy as np

for i in xrange(1, t + 1):
    D, N = [s for s in raw_input().split(" ")]
    D = int(D) #destination distance
    N = int(N) #number of horses
    K = np.zeros(N) #start position
    S = np.zeros(N) #speed
    T = np.zeros(N) #arrival time
    for j in xrange(0,N):
        string = raw_input().split(" ")
        K[j] = int(string[0]) #starting position of jth horse
        S[j] = int(string[1]) #speed of jth horse
        T[j] = float(D-K[j])/float(S[j])

    time = max(T)
    optimal_speed = D / float(time)

    print "Case #{}: {}".format(i, optimal_speed)
