#!/usr/bin/env python
# -*- coding:utf-8 -*-

def solve(s_list):
    stand = 0
    add   = 0
    for s, n in enumerate(s_list):
        if n == 0:
            continue

        if s <= stand:
            stand += n
        else:
            add   += s - stand
            stand += n + add
    return add


def main():
    # test case num
    t_num = int(raw_input())

    for t in xrange(t_num):
        max_s, s_str = raw_input().split()

        s_list = []
        for i, n in enumerate(s_str):
            s_list.append(int(n))
        num = solve(s_list)
        print "Case #{}: {}".format(t+1, num)


if __name__ == "__main__":
    main()
