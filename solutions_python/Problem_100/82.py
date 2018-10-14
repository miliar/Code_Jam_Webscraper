#!/usr/bin/python

import sys


def get_min_plays(N, req_stars):
    req_stars.sort(cmp=lambda x, y: y[1] - x[1])
    done = [0 for i in req_stars]

    cur_stars = 0
    plays = 0
    levels_done = 0

    while (levels_done < N):
        two_star_found = False
        one_star_found = False

        for i in range(len(req_stars)):
            if (done[i] < 2):
                if (cur_stars >= req_stars[i][1]):
                    two_star_found = True
                    if (done[i] == 1):
                        cur_stars += 1
                    else:
                        cur_stars += 2
                    done[i] = 2
                    levels_done += 1
                    plays += 1
                    break

        if (two_star_found == False):
            for i in range(len(req_stars)):
                if (done[i] == 0):
                    if (cur_stars >= req_stars[i][0]):
                        done[i] = 1
                        one_star_found = True
                        plays += 1
                        cur_stars += 1
                        break

        if ((one_star_found == False) and (two_star_found == False)):
            return None

    return plays

if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for i in range(1, T + 1):
        N = int(sys.stdin.readline().strip())
        req_stars = []
        for j in range(N):
            a, b = tuple([int(k) for k in sys.stdin.readline().strip().split()])
            req_stars.append((a, b))
        mn = get_min_plays(N, req_stars)
        if (mn is None):
            print "Case #{0}: Too Bad".format(i)
        else:
            print "Case #{0}: {1}".format(i, mn)
