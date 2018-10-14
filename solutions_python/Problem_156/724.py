import sys
import bisect
import math
import copy

def exec_test(P):
    D = len(P)
    max_after_split = math.ceil(P[0] / 2)
    special_minutes = 0
    min_turns = P[0]
    min_special_minutes = 0

    for j in range(D):
        special_minutes += 1
        if P[j] <= max_after_split:
            break

        if j + 1 >= D:
            newmin = max_after_split + special_minutes
        else:
            newmin = max(max_after_split + special_minutes, P[j + 1] + special_minutes)

        if newmin < min_turns:
            changed = True
            min_turns = newmin
            min_special_minutes = special_minutes

    nPs = [P]
    for k in range(min_special_minutes):
        nnPs = []
        for l in nPs:
            nP = copy.deepcopy(l)
            nP2 = copy.deepcopy(l)

            oldP = nP[0]

            del nP[0]
            del nP2[0]

            gr = math.ceil(oldP / 2)
            sm = math.floor(oldP / 2)

            reverse_insort(nP2, gr)
            reverse_insort(nP2, sm)
            nnPs.append(nP2)

            if (gr % 2) != 0:
                gr += 1
                sm -= 1

                reverse_insort(nP, gr)
                reverse_insort(nP, sm)

                nnPs.append(nP)


        nPs = nnPs

    if min_special_minutes != 0:
        return min([min_special_minutes + exec_test(arg) for arg in nPs])
    else:
        return P[0]


def reverse_insort(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it reverse-sorted assuming a
    is reverse-sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x > a[mid]:
            hi = mid
        else:
            lo = mid + 1
    a.insert(lo, x)


fd = open("./B-small.in", "r")
fout = open("./B-small.out", "w")

num_tests = int(fd.readline().strip())

for i in range(num_tests):
    D = int(fd.readline().strip())

    P = sorted([int(x) for x in fd.readline().strip().split(" ")])
    P.reverse()

    used_special_minutes = exec_test(P)
    print("Case #{}: {}".format(i + 1, used_special_minutes))
    fout.write("Case #{}: {}".format(i + 1, used_special_minutes) + "\n")

fout.close()
fd.close()