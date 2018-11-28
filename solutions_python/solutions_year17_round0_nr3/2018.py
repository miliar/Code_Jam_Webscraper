import sys
from operator import itemgetter


def solve(n, k):
    if n == k:
        return (0, 0)

    minlr = maxlr = 0
    EMPTY = 0
    OCCUPIED = 1
    rooms = [EMPTY] * (n + 2)
    rooms[0] = OCCUPIED
    rooms[-1] = OCCUPIED

    while k > 0:
        ls = [0] * (n + 2)
        rs = [0] * (n + 2)
        for i in range(1, n + 1):
            if rooms[i] == OCCUPIED:
                continue

            # calculate the ls and rs values
            if rooms[i - 1] == OCCUPIED:
                # this is an empty room, next to an occupied room
                for prev_room in range(i - 1, -1, -1):
                    if rooms[prev_room] == OCCUPIED:
                        break
                    ls[i] += 1
                for next_room in range(i + 1, n + 3):
                    if rooms[next_room] == OCCUPIED:
                        break
                    rs[i] += 1
            else:
                # this is an empty room, which also had an empty room to its left
                # use the ls an rs values calculated for the previous room to save
                # unnecessary computation
                ls[i] = ls[i - 1] + 1
                rs[i] = rs[i - 1] - 1

        # place the person in the appropriate room
        minlsrs = [min(l, r) for l, r in zip(ls, rs)]
        fil_ind_minlsrs = [(i, v) for i, v in enumerate(minlsrs)
                           if rooms[i] == EMPTY]

        maxlsrs = [max(l, r) for l, r in zip(ls, rs)]

        max_minlsrs = max(fil_ind_minlsrs, key=itemgetter(1))[1]

        index = -1
        if count_occ(fil_ind_minlsrs, max_minlsrs) == 1:
            index = find(fil_ind_minlsrs, max_minlsrs)
        else:
            # multiple rooms with minlsrs = max_minlsrs
            # consider rooms with max_minlsrs that have max_maxlsrs
            max_minlsrs_indices = [
                i for i, v in fil_ind_minlsrs if v == max_minlsrs
            ]
            filtered_maxlsrs = [(i, v) for i, v in enumerate(maxlsrs)
                                if i in max_minlsrs_indices]
            max_maxlsrs = max(filtered_maxlsrs, key=itemgetter(1))[1]
            index = find(filtered_maxlsrs, max_maxlsrs)

        rooms[index] = OCCUPIED
        maxlr, minlr = maxlsrs[index], minlsrs[index]
        k -= 1

    return (maxlr, minlr)


def count_occ(l, x):
    count = 0
    for i, v in l:
        if v == x:
            count += 1


def find(l, x):
    for i, v in l:
        if v == x:
            return i


if __name__ == "__main__":
    infile = None
    if len(sys.argv) == 2:
        # debug mode
        infile = open("c_bathroom_stalls.in")

        def input():
            return infile.readline()

    t = int(input())
    for caseno in range(1, t + 1):
        n, k = [int(v) for v in input().strip().split()]
        result = solve(n, k)
        print("Case #{}: {} {}".format(caseno, result[0], result[1]))

    if len(sys.argv) == 2:
        infile.close()
