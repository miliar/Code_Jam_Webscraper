#!/usr/bin/env python
# -*- coding: utf-8 -*

"""GCJ Round 1B: Problem A. Osmos"""


def solve(s, n, tab):
    out = 0
    tab.sort()
#    print(s)

    for k in range(n):
        mote = tab[k]
        if mote < s:
            s += mote
#            print(s, 0)
        else:
            diff = mote - s
#            print("\tdiff", diff)
            if diff == 0:
                if s != 1:
                    s += (s - 1)
#                    print(s, 1)
                    s += mote
                out += 1
#                print(s, 11, out)
            else:
                old_s = s
                nb_op = 0
                while mote >= s and nb_op < len(tab[k:]):
                    s += (s - 1)
                    nb_op += 1
#                    print(s, 2, out)
                out += nb_op
                if mote < s:
                    s += mote
                else:
                    break
#                print(s, 22, out)

    return out


if __name__ == "__main__":
    T = int(input())  # nb of test cases

    for x in range(T):
        A, N = map(int, input().split())
        sizes = [int(k) for k in input().split()]

        y = solve(A, N, sizes)
        print("Case #%d: %s" % (x+1, y))
