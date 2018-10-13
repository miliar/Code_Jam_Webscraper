#!/usr/bin/python2.7

from decimal import Decimal


def calc_time_for_amount_farms(farm_cost, additional_farm_rate, target_amount, amount_farms):
    time = 0.0
    default_rate = 2.0

    i = 0
    while i < amount_farms:
        time += (farm_cost / (default_rate + (additional_farm_rate * i)))
        i += 1

    time += (target_amount / (default_rate + (additional_farm_rate * i)))

    return time



def process_testcase(cn, f, fout):
    vals = f.readline().strip().split(" ")

    farm_cost = float(vals[0])
    additional_farm_rate = float(vals[1])
    target_amount = float(vals[2])

    ##print farm_cost
    #print additional_farm_rate
    #print target_amount


    i = 0

    old_t = 9999999
    new_t = calc_time_for_amount_farms(farm_cost, additional_farm_rate, target_amount, 0)

    while new_t <= old_t:
        i += 1

        old_t = new_t
        new_t = calc_time_for_amount_farms(farm_cost, additional_farm_rate, target_amount, i)

        #print new_t

    fout.write("Case #"+str(cn)+": %0.7f\n" % old_t)

f = open("QualProblemB.in")
fout = open("QualProblemB.out", "w")

amount_testcases = int(f.readline())

for i in range(0, amount_testcases):
    print i
    process_testcase(i + 1, f, fout)