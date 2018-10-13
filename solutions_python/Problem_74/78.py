# -*- coding: utf-8 -*-

INPUT_FILE_PATH = "A-large-975485.in"
OUTPUT_FILE_PATH = "A-large-975485.out"

INIT_STATE = 1
ORANGE_STATE = 2
BLUE_STATE = 3

fr = open(INPUT_FILE_PATH, 'r')
fw = open(OUTPUT_FILE_PATH, 'w')

T = int(fr.readline().strip())

for i in range(T):
    tmp_list = fr.readline().strip().split()
    N = int(tmp_list.pop(0))
    o_cur_pos = 1
    b_cur_pos = 1
    total_cost = 0
    tmp_cost = 0
    state_flag = INIT_STATE
    for j in range(N):
        tmp_color = tmp_list.pop(0)
        dest = int(tmp_list.pop(0))
        # print tmp_color, dest, tmp_cost, total_cost
        if tmp_color == 'O':
            if state_flag != ORANGE_STATE:
                total_cost += tmp_cost
                state_flag = ORANGE_STATE
                if abs(dest - o_cur_pos) < tmp_cost:
                    tmp_cost = 1
                else:
                    tmp_cost = abs(dest - o_cur_pos) - tmp_cost + 1
            else:
                tmp_cost += abs(dest - o_cur_pos) + 1
            o_cur_pos = dest
        elif tmp_color == 'B':
            if state_flag != BLUE_STATE:
                total_cost += tmp_cost
                state_flag = BLUE_STATE
                if abs(dest - b_cur_pos) < tmp_cost:
                    tmp_cost = 1
                else:
                    tmp_cost = abs(dest - b_cur_pos) - tmp_cost + 1
            else:
                tmp_cost += abs(dest - b_cur_pos) + 1
            b_cur_pos = dest
    total_cost += tmp_cost
    fw.write("Case #%d: %d\n" % (i + 1, total_cost))
