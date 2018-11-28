#!/usr/bin/env python

ncase = int(raw_input())
for casenu in range(1, ncase + 1):
    line_data = raw_input().split()
    pos = 0
    def read_ele():
        global pos, line_data
        ret = line_data[pos]
        pos += 1
        return ret

    dict_combine = dict()
    for i in range(int(read_ele())):
        s = read_ele()
        dict_combine[(s[0], s[1])] = s[2]
        dict_combine[(s[1], s[0])] = s[2]

    set_oppose = set()
    for i in range(int(read_ele())):
        s = read_ele()
        set_oppose.add((s[0], s[1]))
        set_oppose.add((s[1], s[0]))

    seq = read_ele()
    seq = read_ele()
    rst = list()
    for ch in seq:
        if rst:
            pair = (rst[-1], ch)
            if pair in dict_combine:
                rst[-1] = dict_combine[pair]
                continue
            ok = True
            for i in rst:
                if (i, ch) in set_oppose:
                    ok = False
                    break
            if not ok:
                rst = list()
                continue
        rst.append(ch)

    print ("Case #%d: [" % casenu) + ", ".join(rst) + "]"

