import sys
import math


def answer(N, K, info):
    rh_sorted = sorted(info, key=lambda x: x[0]*x[1], reverse=True)

    max_r_start = max([item[0] for item in rh_sorted[:K]])
    res = 2* sum([item[0]*item[1] for item in rh_sorted[:K]]) + max_r_start*max_r_start

    if K < N:
        max_rsq_rh = max([(item[0]+2 * item[1])*item[0] for item in rh_sorted[K:]])
        res2 =  2* sum([item[0]*item[1] for item in rh_sorted[:K-1]]) + max_rsq_rh
        res = max([res, res2])

    return res * math.pi

if __name__ == "__main__":

    T = int(sys.stdin.next())
    queries = []
    for i in range(T):
        N, K = map(int, sys.stdin.next().split(' '))
        info = []
        for j in range(N):
            R, H = map(int, sys.stdin.next().split(' '))
            info.append((R, H))
        queries.append((N, K, info))
    for i, q in enumerate(queries):
        print "".join(["Case #", str(i+1), ": ", str(round(answer(*q), 8))])

