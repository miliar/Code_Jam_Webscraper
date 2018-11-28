"""
Skeleton to solve problems
"""
import sys
import numpy as np
from copy import deepcopy

f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    l = map(int, f.readline().strip().split(" "))
    order = "ROYGBV"
    N, hc = l[0], l[1:]
    out = []
    prev_i = None
    for i in range(N):
        if prev_i is None:
            hc_tmp = hc
        else:
            hc_tmp = deepcopy(hc)
            hc_tmp[prev_i] = -1
        curr_i = np.argmax(hc_tmp)
        if hc_tmp[curr_i] <= 0:
            break
        if prev_i is None:
            first_i = curr_i
        elif (prev_i != first_i) and \
             (hc[curr_i] == hc[first_i]):  # give preference to first
            curr_i = first_i
        out.append(order[curr_i])
        hc[curr_i] -= 1
        prev_i = curr_i
    result = "IMPOSSIBLE" if N > 1 and ((out[0] == out[-1]) or sum(hc) > 0) \
        else "".join(out)
    if result != "IMPOSSIBLE":
        for i in range(N):
            (a, b) = (0, N-1) if i == N-1 else (i, i+1)
            if out[a] == out[b]:
                print out
                raise

    print("Case #%d: %s" % (c+1, str(result)))

f.close()
