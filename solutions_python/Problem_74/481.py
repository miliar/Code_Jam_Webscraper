#!/usr/bin/python

t = int(raw_input())

for i in xrange(t):
    l = raw_input().split()
    ob = zip(l[1::2],map(int,l[2::2]))
    o = []
    b = []
    for (color, button) in ob:
        if color == 'O':
            o.append(button)
        elif color == 'B':
            b.append(button)

    count = 0
    o_s = 1
    o_i = 0
    b_s = 1
    b_i = 0
    for x in ob:
        if x[0] == 'O':
            n = abs(x[1] - o_s) + 1
            o_s = x[1]
            o_i += 1

            if b_i < len(b):
                if b_s < b[b_i]:
                    if b_s + n <= b[b_i]:
                        b_s += n
                    else:
                        b_s = b[b_i]
                elif b_s > b[b_i]:
                    if b_s - n >= b[b_i]:
                        b_s -= n
                    else:
                        b_s = b[b_i]
        elif x[0] == 'B':
            n = abs(x[1] - b_s) + 1
            b_s = x[1]
            b_i += 1

            if o_i < len(o):
                if o_s < o[o_i]:
                    if o_s + n <= o[o_i]:
                        o_s += n
                    else:
                        o_s = o[o_i]
                elif o_s > o[o_i]:
                    if o_s - n >= o[o_i]:
                        o_s -= n
                    else:
                        o_s = o[o_i]

        count += n

    print("Case #%d: %d" % (i+1, count))


