import common
import copy
import math
import Queue

def compute_solution(Q,counts):
    if len(Q) == 0: return 0
    _,m = common.pop(Q)
    k = counts.pop(m)
    best = m
    if m>1:
        for a in range(1,m):
            child_Q = copy.deepcopy(Q)
            child_counts = copy.deepcopy(counts)
            b = m - a
            common.push(child_Q,child_counts,a,k)
            common.push(child_Q,child_counts,b,k)
            best = min(best, compute_solution(child_Q,child_counts) + k)
    else:
        best = 1
    common.push(Q,counts,m,k)
    return best

T = int(raw_input())
for i in range(T):
    Q,counts = common.load_data()
    time = compute_solution(Q,counts)
    print "Case #%d: %d"%(i+1,time)
