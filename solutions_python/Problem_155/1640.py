#! /usr/local/python

T = int(raw_input())
for test in range(T):
    s_max, s_arr = raw_input().split()
    s_max = int(s_max)
    s_arr = [int(i) for i  in s_arr ]
    ts = 0
    tr = 0
    index = 0
    for i in s_arr:
        if index <= ts:
            ts += i
        elif not i == 0:
            temp = (index - ts)
            tr += temp
            ts += (temp + i)
        index += 1
    print 'Case #%d:'% (test+1),
    print tr
