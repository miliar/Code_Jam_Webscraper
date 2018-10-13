#!/usr/bin/python

pot2 = []
for i in range(31):
    pot2.append((2**i)-1)

for case in range(input()):
    R, k, N = map(int, raw_input().split())
    g = map(int, raw_input().split())

    travels = []
    t_ini = []
    t_loop = []
    if (sum(g) <= k):
        travels.append(sum(g))
        t_loop = travels[:]
    else:
        process_pos = []
        pos = 0
        pos_ant = -1
        while (not pos in process_pos):
            process_pos.append(pos)
            pos_ant = pos
            people = 0
            full = False
            while (not full):
                if (people + g[pos] <= k):
                    people += g[pos]
                    pos += 1
                    if (pos >= len(g)):
                        pos = 0
                else:
                    full = True
                if (pos == pos_ant):
                    full = True
            travels.append(people)
        i = 0
        while (i < len(process_pos)) and (process_pos[i] != pos):
            i += 1
        t_ini = travels[:i]
        t_loop = travels[i:]

    money = 0
    if (R < len(t_ini)):
        money = sum(t_ini[:R])
        R = 0
    else:
        money = sum(t_ini)
        R = R - len(t_ini)

    if (R > 0):
        complete_loops = 0
        if (R > len(t_loop)):
            complete_loops = R // len(t_loop)
        parcial_loop = R - (complete_loops*len(t_loop))
        if (complete_loops > 0):
          money += complete_loops * sum(t_loop)
        money += sum(t_loop[:parcial_loop])

    print 'Case #%s: %d' % (case+1, money)
