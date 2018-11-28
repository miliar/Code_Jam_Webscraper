#!/usr/local/bin/python3

import sys


i_nb_test_cases = int(sys.stdin.readline())
#print (repr(i_nb_test_cases))

for i in range(1, i_nb_test_cases + 1):
    l_input = sys.stdin.readline().split()
    f_C = float(l_input[0])
    f_F = float(l_input[1])
    f_X = float(l_input[2])


    f_time_farm_cost = 0
    i_iteration = 0
    f_best_time = f_X / 2.0
    while True:
        i_iteration += 1

        f_new_time = f_X / (2.0 + (i_iteration) * f_F)
        f_time_farm_cost += f_C / (2.0 + (i_iteration - 1) * f_F)
        f_new_time += f_time_farm_cost

        if (f_best_time > f_new_time):
            f_best_time = f_new_time
        else:
            break

    print ('Case #', i, ': ', "{:.7f}".format(f_best_time), sep='')
