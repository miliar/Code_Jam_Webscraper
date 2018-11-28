#!/usr/bin/env python

import sys
from operator import itemgetter
import math

def process_input():
    with open("input.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def print_result(global_counter, r):
    print "Case #" + str(global_counter) + ": %.9f" % r


def single_run(N, K, data, global_counter):
    global g_counter
    # if global_counter == 79:
    #     print N, K
    #     print data
    # print N, K
    R_lst = []
    H_lst = []
    p = 3.141592653589793238462643
    for i in range(0, N):
        R_i = int(data[i].split(' ')[0])
        H_i = int(data[i].split(' ')[1])
        surface = p * R_i * R_i
        side = 2*p*R_i*H_i
        R_lst.append([R_i, H_i, surface + side, surface, side])
        H_lst.append([R_i, H_i, surface + side, surface, side])
    R_lst = list(reversed(sorted(R_lst, key=itemgetter(3))))
    H_lst = list(reversed(sorted(H_lst, key=itemgetter(4))))
    R_largest = R_lst[0]
    R_l_i = H_lst.index(R_largest)
    rtn = 0.0

    if K == 1:
        tmp_tmp = list(reversed(sorted(R_lst, key=itemgetter(2))))
        return tmp_tmp[0][2]

    if R_l_i < K:
        for i in range(0, K):
            rtn += H_lst[i][4]
        rtn += R_largest[3]
        return rtn
    else:
        H_lst_tmp_1 = H_lst[0:K]
        for i in range(0, K-1):
            rtn += H_lst[i][4]
        H_smallest = H_lst_tmp_1[len(H_lst_tmp_1) - 1]
        H_lst_tmp_2 =list(reversed(sorted(H_lst_tmp_1, key=itemgetter(3))))
        # print R_largest[2], H_lst_tmp_1[0][4], H_smallest[2], H_lst_tmp_2[0][3]
        if R_largest[2] > (H_smallest[4] + H_lst_tmp_2[0][3]):

            rtn = rtn + R_largest[3] + R_largest[4]
        else:

            rtn += H_smallest[4]
            # H_lst_tmp_2 =list(reversed(sorted(H_lst_tmp_1, key=itemgetter(3))))
            rtn += H_lst_tmp_2[0][3]
        return rtn

def main():
    content = process_input()
    data_size = int(content.pop(0))
    global_counter = 1
    i = 0
    while True:
        N = int(content[i].split(' ')[0])
        K = int(content[i].split(' ')[1])
        rtn = single_run(N, K, content[i + 1:i + 1 + N], global_counter)
        print_result(global_counter, rtn)
        i += 1 + N
        global_counter += 1
        if global_counter == data_size + 1:
            break

main()
