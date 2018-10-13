#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math

def get_first_bigger(choosen, list_t):
    for i in range(len(list_t)):
        if list_t[i] > choosen:
            return i

    return -1

def get_rand(bot, up, list):
    while True:
        r = random.uniform(bot+0.000001, up)
        for item in list:
            if abs(item-r) < 0.000001:
                continue
        return r

def solve_it(input_data):

    f = open('round1D.out', 'w')

    # parse the input
    lines = input_data.split('\n')

    num_of_case = int(lines[0])
    lines = lines[1:]

    for z in range(num_of_case):
        print 'case: ', z+1
        naomi_list_org = lines[z*3+1].split(' ')
        ken_list_org = lines[z*3+2].split(' ')

        for i in range(len(naomi_list_org)):
            naomi_list_org[i] = float(naomi_list_org[i])
            ken_list_org[i] = float(ken_list_org[i])

        naomi_list = sorted(naomi_list_org)
        ken_list = sorted(ken_list_org)

        n_point = 0

        while len(naomi_list) > 0:
            current_size = len(naomi_list)
            choosen_naomi = None
            told_naomi = None
            choosen_ken = None

            max_nami = naomi_list[current_size-1]
            min_nami = naomi_list[0]
            min_ken = ken_list[0]
            max_ken = ken_list[current_size-1]

            if (max_nami < min_ken) or (max_ken < min_nami):
                # print 't1'
                choosen_naomi = naomi_list.pop(0)
                choosen_ken = ken_list.pop(0)
            else:
                can_duoi = max(min_ken, min_nami)
                can_tren = min(max_ken, max_nami)

                told_naomi = get_rand(can_duoi, can_tren, ken_list)
                index = get_first_bigger(told_naomi, ken_list)
                choosen_ken = ken_list.pop(index)

                index2 = get_first_bigger(choosen_ken, naomi_list)
                if index2 != -1:
                    choosen_naomi = naomi_list.pop(index2)
                else:
                    choosen_naomi = naomi_list.pop(0)
            
            # print 'told_naomi: ', told_naomi
            # print 'choosen_naomi', choosen_naomi
            # print 'choosen_ken', choosen_ken

            if choosen_naomi > choosen_ken:
                n_point += 1


        n_2 = 0
        naomi_list2 = [n for n in naomi_list_org]
        ken_list2 = [k for k in ken_list_org]
        naomi_list2 = sorted(naomi_list2)
        ken_list2 = sorted(ken_list2)

        print naomi_list2
        print ken_list2

        while len(naomi_list2) > 0:
            c_n = naomi_list2.pop()
            k_n = None
            tmp_index = get_first_bigger(c_n, ken_list2)
            if tmp_index != -1:
                k_n = ken_list2.pop(tmp_index)

            else:
                k_n = ken_list2.pop(0)

            if c_n > k_n:
                n_2 += 1

            # print c_n, k_n

        # print 'n_point %d' % (n_point)
        # print 'n_point %d \n ***' % (n_2)
        f.write('Case #' + str(z+1) + ': ' + str(n_point) + ' ' + str(n_2) + '\n')


    # f.close()
    return None


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.'

