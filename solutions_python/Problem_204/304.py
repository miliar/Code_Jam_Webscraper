#!/usr/bin/env python

import sys
import math

def process_input():
    with open("B-small-attempt3.in") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def print_result(global_counter, r):
    print "Case #" + str(global_counter) + ":", r

def determine():
    return True

def check_lst_eq(lst, avg):
    i = 0
    pre = -1
    while i < len(lst):
        cur = lst[i]
        if cur > avg*1.1 or cur < avg*0.9:
            return False
        i += 1
    return True


def single_run(N, P, data, global_counter):
    final_result = 0
    R = list()
    R = [int(x) for x in data[0].split(' ')]
    Q = dict()
    j = 0
    while j < N:
        Q[j] = [int (x) for x in data[1 + j].split(' ')]
        Q[j].sort()
        iii = 0
        while iii < len(Q[j]):
            cur_val = Q[j][iii]
            cur_quot = float(Q[j][iii]) / float(R[j])
            cur_floor = math.floor(cur_quot)
            cur_ceil = math.ceil(cur_quot)
            if cur_quot - cur_floor > cur_ceil - cur_quot:
                to_cmp = cur_ceil
                # print cur_quot, cur_ceil
                tmp_val = float(cur_quot) / cur_ceil
                if  tmp_val >= 0.9 and tmp_val <= 1.1:
                    iii +=1
                else:
                    Q[j].pop(iii)
            else:
                to_cmp = 1 if cur_floor < 1 else cur_floor
                tmp_val = float(cur_quot) / to_cmp
                if  tmp_val >= 0.9 and tmp_val <= 1.1:
                    iii +=1
                else:
                    Q[j].pop(iii)
        j += 1
    # print_result(global_counter, data)
    # print N, P, Q, data
    j = 0
    while True:
        jjj = 0
        while jjj < N:
            if len(Q[jjj]) == 0:
                print_result(global_counter, final_result)
                return
            jjj += 1
        tmp = list()
        i = 0
        while i < N:
            perc = float(Q[i][0]) / float(R[i])
            tmp.append(perc)
            i += 1
        tmp_2 = [int(math.floor(x)) if ((x - math.floor(x)) < (math.ceil(x) - x)) else int(math.ceil(x)) for x in tmp]
        lst_avg = float(sum(tmp_2)) / len(tmp_2)
        rtn1 = check_lst_eq(tmp, math.ceil(lst_avg))
        rtn2 = check_lst_eq(tmp, math.floor(lst_avg))
        max_val = lst_avg
        min_val = sorted(tmp)[0]
        if rtn1 or rtn2:
            final_result += 1
            jjj = 0
            while jjj < N:
                Q[jjj].pop(0)
                jjj += 1
        else:
            jjj = 0
            while jjj < N:
                if tmp[jjj] == min_val:
                    Q[jjj].pop(0)
                    break
                jjj += 1
def main():
    content = process_input()
    data_size = int(content.pop(0))
    global_counter = 1
    i = 0
    while True:
        N = int(content[i].split(' ')[0])
        P = int(content[i].split(' ')[1])
        single_run(N, P, content[i + 1: i + 2 + N], global_counter)
        i += 2 + N
        global_counter += 1
        if global_counter == data_size + 1:
            break

main()
