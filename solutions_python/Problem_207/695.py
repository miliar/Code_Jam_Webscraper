#!/usr/bin/env python

# Google Code Jam
# Google Code Jam 2017
# Round 1B 2017
# Problem B. Stable Neigh-bors


from __future__ import print_function, division
import heapq

def is_valid(stall):
    for i, c in enumerate(stall):
        try:
            if stall[i] == stall[i+1]:
                return False
        except IndexError:
            if stall[0] == stall[-1]:
                return False
    return True

def make_stall(n, r, o, y, g, b, v):
    stall = ['?'] * n
    color_name = 'ROYGBV'
    colors = [r, o, y, g, b, v]
    double_colors = (o, g, v)
    if any(color/sum(colors) > 0.5 for color in colors):
        return 'IMPOSSIBLE'

    if sum(double_colors) / sum(colors) > 0.5:
        return 'IMPOSSIBLE'

    if sum(double_colors) / sum(colors) > 1/3 and double_colors.count(0) < 2:
        return 'IMPOSSIBLE'

    if o > 2*b:
        return 'IMPOSSIBLE'

    if g > 2*r:
        return 'IMPOSSIBLE'

    if v > 2*y:
        return 'IMPOSSIBLE'

    if sum(double_colors) == 0:
        if r == y == b:
            return 'RYB' * int(n/3)
        elif r == 0:
            return 'YB' * int(n/2)
        elif y == 0:
            return 'RB' * int(n/2)
        elif b == 0:
            return 'RY' * int(n/2)
        else:
            rank = heapq.nlargest(n, range(len(colors)), key=colors.__getitem__)
            max_color = color_name[rank[0]]
            sec_max_color = color_name[rank[1]]
            third_max_color = color_name[rank[2]]

            stall = 'RYB' * colors[rank[2]]
            colors[rank[0]] += - colors[rank[2]]
            colors[rank[1]] += - colors[rank[2]]
            # print(max_color, sec_max_color, third_max_color)

            alt_dict = {
                'R': ['BY', 'YB'],
                'Y': ['BR', 'RB'],
                'B': ['RY', 'YR']
            }

            turn = 0
            while colors[rank[0]] + colors[rank[1]] > 0:
                # print(stall)
                turn += 1

                if colors[rank[0]] > 0 and turn % 2 == 0:
                    alt_0 = alt_dict[max_color][0][0]
                    alt_1 = alt_dict[max_color][0][1]
                    try:
                        index = stall.index(alt_dict[max_color][0])
                        # print('67', index)
                        stall = stall[:index+1] + max_color + stall[index+1:]
                        colors[rank[0]] += -1
                        continue
                    except ValueError:
                        try:
                            index = stall.index(alt_dict[max_color][1])
                            # print('74', index)

                            stall = stall[:index+1] + max_color + stall[index+1:]
                            colors[rank[0]] += -1
                            continue
                        except ValueError:
                            if (stall[0] == alt_0 and stall[-1] == alt_1) or (stall[0] == alt_1 and stall[-1] == alt_0):
                                # print('81')
                                stall += max_color
                                colors[rank[0]] += -1
                                continue
                            else:
                                return 'IMPOSSIBLE'

                if colors[rank[1]] > 0 and turn % 2 == 1:
                    alt_0 = alt_dict[sec_max_color][0][0]
                    alt_1 = alt_dict[sec_max_color][0][1]
                    try:
                        index = stall.index(alt_dict[sec_max_color][0])
                        stall = stall[:index+1] + sec_max_color + stall[index+1:]
                        colors[rank[1]] += -1
                        continue
                    except ValueError:
                        try:
                            index = stall.index(alt_dict[sec_max_color][1])
                            stall = stall[:index+1] + sec_max_color + stall[index+1:]
                            colors[rank[1]] += -1
                            continue
                        except ValueError:
                            if (stall[0] == alt_0 and stall[-1] == alt_1) or (stall[0] == alt_1 and stall[-1] == alt_0):
                                stall += sec_max_color
                                colors[rank[1]] += -1
                                continue
                            else:
                                return 'IMPOSSIBLE'


            # for _ in range(colors[rank[0]] - colors[rank[2]]):
            #     for i in range(len(stall)):
            #         print(range(len(stall)))
            #         if i < len(stall)-1:
            #             print(i, len(stall))
            #             print(stall[i], stall[i+1])
            #             if stall[i] != max_color and stall[i+i] != max_color:
            #                 stall = stall[:i+1] + max_color + stall[i+1:]
            #                 break
            #         else:
            #             if stall[i] != max_color and stall[0] != max_color:
            #                 stall += max_color
            #                 break
            #
            # for _ in range(colors[rank[1]] - colors[rank[2]]):
            #     for i in range(len(stall)):
            #         if i < len(stall)-1:
            #             if stall[i] != sec_max_color and stall[i+i] != sec_max_color:
            #                 stall = stall[:i+1] + sec_max_color + stall[i+1:]
            #                 break
            #         else:
            #             if stall[i] != sec_max_color and stall[0] != sec_max_color:
            #                 stall += sec_max_color
            #                 break

            assert len(stall) == n
            assert is_valid(stall)

            return stall

    else:
        stall = ''.join(stall)
        assert len(stall) == n

        return stall

if __name__ == '__main__':
    import os

    samples = [
        (6, 2, 0, 2, 0, 2, 0),
        (3, 1, 0, 2, 0, 0, 0),
        (6, 2, 0, 1, 1, 2, 0),
        (4, 0, 0, 2, 0, 0, 2),
        (4, 2, 0, 1, 0, 1, 0)
    ]

    for sample in samples:
        print(make_stall(*sample))

    data_files = ['B-small-attempt3', ]
    # 'B-large-practice']
    for f in data_files:
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.in'.format(f)), 'r') as input_file:
            lines = input_file.readlines()
        input_count = int(lines[0].replace('\n' ,''))
        inputs = [line.replace('\n', '') for line in lines[1:]]

        i = 1
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),
                  '{0}.out'.format(f)), 'w') as output_file:
            for line in inputs:
                test_case = tuple([int(_) for _ in line.split(' ')])
                stall = make_stall(*test_case)
                output_file.write('Case #{0}: {1}\n'.format(i, stall))

                i += 1
