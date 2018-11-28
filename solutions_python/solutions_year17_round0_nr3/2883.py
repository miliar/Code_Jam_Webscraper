
from __future__ import division
import numpy as np



def solve_stalls(K,N):
    stalls = np.zeros((N+2,1))
    stalls[0]=1
    #stalls[0]=1
    stalls[-1]=1

    for k in range(0,K):

        idx_occ = np.where(stalls[:,0]==1)[0] # where people are


        max_dist = 0
        idx_interest= [0,0]
        for ii in range(0,len(idx_occ)-1):
            dist_tmp = idx_occ[ii+1]-idx_occ[ii]-1 # maximum free stalls between two people
            if (dist_tmp > max_dist) :
                max_dist = dist_tmp
                idx_interest[0] = idx_occ[ii]
                idx_interest[1] = idx_occ[ii+1]

        go_to = int(np.ceil(max_dist/2))
        go_to_idx = idx_interest[0]+go_to
        Ls = go_to_idx - idx_interest[0] -1
        Rs = idx_interest[1] - go_to_idx -1
        y = np.max((Ls,Rs))
        z = np.min((Ls,Rs))
        stalls[go_to_idx] = 1
        #print(stalls)

    return y,z


t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    N, K = [s for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    K = int(K)
    N = int(N)
    y,z = solve_stalls(K,N)


    print "Case #{}: {} {}".format(i, y,z)
  # check out .format's specification for more formatting options
