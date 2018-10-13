import os
from math import log2

input_file = 'A-small.in'
out_file = input_file.replace('.in', '.out')
data = os.path.join(os.path.dirname(__file__), input_file)
data_o = os.path.join(os.path.dirname(__file__), out_file)


with open(data, 'r') as f:
    with open(data_o, 'w+') as ff:
        T = int(f.readline().strip('\n'))
        for case in range(1, T + 1):
            d, n = [int(it) for it in f.readline().strip('\n').split()]
            pos_speed = sorted([[int(it) for it in f.readline().strip('\n').split()]
                                for _ in range(n)], key=lambda ps: ps[0])

            times = [(d - p) / s for [p, s] in pos_speed]

            for i in range(n - 1, 0, -1):
                t_1 = times[i - 1]
                t_2 = times[i]

                pos_1, speed_1 = pos_speed[i - 1]
                pos_2, speed_2 = pos_speed[i]
                if speed_1 <= speed_2:
                    continue
                collision_time = (pos_2 - pos_1) / (speed_1 - speed_2)
                if collision_time < 0 or collision_time > t_1:
                    continue
                times[i - 1] = collision_time + \
                               (d - pos_1 - speed_1 * collision_time) / speed_2
            t = times[0]
            s = d / t
            ff.write('Case #%d: %s\n' % (case, s))

