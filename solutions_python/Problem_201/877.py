import sys
import heapq

def solve(N, K):
    heap = []
    size_access = {}
    num = 0
    starter_pair = calc_pair(-N)
    heapq.heappush(heap, starter_pair)
    size_access[starter_pair] = 1
    while heap:
        val = heapq.heappop(heap)
        size = size_access[val]
        del size_access[val]
        num += size
        if K <= num:
            return " ".join( map(lambda x : str(-x), val))
        else:
            fv = val[0]
            sv = val[1]
            if fv != 0:
                fv_pair = calc_pair(fv)
                if fv_pair in size_access:
                    size_access[fv_pair] += size
                else:
                    size_access[fv_pair] = size
                    heapq.heappush(heap, calc_pair(fv))
            if sv != 0:
                sv_pair = calc_pair(sv)
                if sv_pair in size_access:
                    size_access[sv_pair] += size
                else:
                    size_access[sv_pair] = size
                    heapq.heappush(heap, calc_pair(sv))
    return "0 0"

def calc_pair(val):
    val = val * -1
    elem = (val - 1) / 2
    if val % 2:
        return (-elem, -elem)
    else:
        return (-(elem+1), -elem)

def solve_simple(N, K):
    sim = [0 for x in range(N+2)]
    sim[0] = 1
    sim[N+1] = 1
    for elem in range(K):
        L = []
        R = []
        free = 0
        for x in range(N+2):
            if sim[x] == 0:
                L.append(free)
                free += 1
            else:
                L.append(0)
                free = 0
        free = 0
        for y in range(N+2-1, -1, -1):
            if sim[y] == 0:
                R.append(free)
                free += 1
            else:
                R.append(0)
                free = 0
        R = R[::-1]
        minN = -1
        maxN = -1
        minInd = -1
        for x in range(1, N+2):
            if sim[x] == 0:
                tminL = L[x]
                tminR = R[x]
                if minInd == -1:
                    minInd = x
                    minN = min(tminL, tminR)
                    maxN = max(tminL, tminR)
                elif min(tminL, tminR) == minN and max(tminL, tminR) > maxN:
                    minInd = x
                    minN = min(tminL, tminR)
                    maxN = max(tminL, tminR)
                elif min(tminL, tminR) > minN:
                    minInd = x
                    minN = min(tminL, tminR)
                    maxN = max(tminL, tminR)
        if minInd != -1:
            sim[minInd] = 1
    return " ".join([str(maxN), str(minN)])

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for case in range(T):
        N,K = map(int, sys.stdin.readline().split())
        print "Case #{}: {}".format(case+1, solve(N, K))
