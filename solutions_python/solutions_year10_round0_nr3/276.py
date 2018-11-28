#-*-coding:utf-8-*-

import sys
fh = open(sys.argv[1])
T = int(fh.readline())
for cn in range(T):
    R, k, N = [int(x) for x in fh.readline().split(' ')]
    groups = [int(x) for x in fh.readline().split(' ')]
    #print(R, k, N, groups)
    top_g = 0
    filled = 0
    i = 0
    num_rides = 0
    earned = 0
    loops = {}
    while num_rides < R:
        i = top_g
        if i not in loops:
            loops[i] = num_rides, earned
        else:
            nr_, ea_ = loops[i]
            euro = earned - ea_
            period = num_rides - nr_
            rides_remnant = (R - num_rides)
            #print(earned)
            #print('cached {0}:{1},{2} => {3}x{4} = {5}'.format(i, nr_, ea_, rides_remnant, euro, euro * (rides_remnant // period)))
            earned += (rides_remnant // period) * euro
            num_rides += (rides_remnant // period) * period
            pass
        filled = 0
        while num_rides < R:
            if filled + groups[i] > k:
                #print("FILLED by {0}+{1}={2}".format(filled, groups[i], filled + groups[i]))
                num_rides += 1
                next = i
                break
            else:
                #print("PUT {0}/{1} people".format(i, groups[i]))
                filled += groups[i]
                i = (i + 1) % N
                if i == top_g: 
                    num_rides += 1
                    next = i
                    break
                pass
            pass
        earned += filled
        #print('{0}th ride ,{1} people, {2} euro'.format(num_rides, filled, earned))
        filled = 0
        top_g = next % N
        pass
    print('Case #{0}: {1}'.format(cn + 1, earned))
    pass

            
