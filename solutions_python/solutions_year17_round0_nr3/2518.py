import sys
import numpy as np # from https://github.com/numpy/numpy


def calc_rs_ls(occupancy):
    n_stalls = len(occupancy)
    rsls = np.zeros((n_stalls, 2))
    rsls[occupancy] = -1
    for i in range(1, n_stalls):
        rsls[i, 0] = rsls[i - 1, 0] + 1 if rsls[i, 0] > -1 else -1

    for i in range(n_stalls - 1, 0, -1):
        rsls[i, 1] = rsls[i + 1, 1] + 1 if rsls[i, 1] > -1 else -1

    return rsls

def handle_case(stalls, people):
    occupancy = np.asarray([True] + [False] * (stalls) + [True])
    #occupancy = [True] + [False] * (stalls) + [True]
    for i in range(people):
        rsls = calc_rs_ls(occupancy)
        min_rsls = np.min(rsls, axis=-1)
        max_min_rsls = np.max(min_rsls)
        max_min_mask = (min_rsls == max_min_rsls)
        max_rsls = np.max(rsls[max_min_mask, :], axis=-1)
        max_max_rsls = np.max(max_rsls)
        if np.sum(max_min_mask) > 1:
            max_max_mask = (max_rsls == max_max_rsls)
            if np.sum(max_max_mask) > 1:
                #print 'changing %s ' % occupancy
                idx = ((np.arange(len(occupancy))[np.where(max_min_mask)])[np.where(max_max_mask)])[0]
                occupancy[idx] = True
                #print 'changed %s ' % occupancy
            else:
                idx = ((np.arange(len(occupancy))[np.where(max_min_mask)])[np.where(max_max_mask)])
                occupancy[idx] = True
        else:
            idx = np.arange(len(occupancy))[np.where(max_min_mask)]
            occupancy[idx] = True
    return max_max_rsls, max_min_rsls

num_cases = int(sys.stdin.readline().strip())

for i in range(num_cases):
    inp = sys.stdin.readline().strip().split()
    N = int(inp[0].strip())
    K = int(inp[1].strip())

    y, z = handle_case(N, K)

    print('Case #%d: %d %d' % (i+1, y, z))