__author__ = 'st_lim'

INITIAL_RATE = 2.0
rates = [INITIAL_RATE]
wait_farm = []
wait_tgt = []
wait_count = []

def stop_wait(count, c, x, f):
    return cal_wait_tgt(count, x, f) > cal_next_tgt(count, c, x, f)

def cal_next_tgt(count, c, x, f):
    if count >= len(wait_count):
        wait_count.append(cal_wait_farm(count, c, f) + cal_wait_tgt(count + 1, x, f))
    return wait_count[count]

# 2000 / 2 + f*count
def cal_wait_tgt(count, x, f):
    if count >= len(wait_tgt):
        wait_tgt.append(x / cal_rate(count, f))
    return wait_tgt[count]

def cal_wait_farm(count, c, f):
    if count >= len(wait_farm):
        wait_farm.append(c / cal_rate(count, f))
    return wait_farm[count]

def cal_rate(count, f):
    if count >= len(rates):
        rates.append(rates[count-1] + f)
    return rates[count]

import sys
myfile = open(sys.argv[1], 'r')
myoutfile = open('output.txt', 'w')
n_cases = int(myfile.readline())
for i in range(1, n_cases + 1):
    c, f, x = map(float, myfile.readline().split())
    count = 0
    total_time = 0.0
    # Reinitialize
    rates = [INITIAL_RATE]
    wait_farm = []
    wait_tgt = []
    wait_count = []
    while stop_wait(count, c, x, f):
        total_time += cal_wait_farm(count, c, f)
        count += 1
    total_time += cal_wait_tgt(count, x, f)
    output = "Case #{0}: {1:.7f}\n".format(i, total_time)
    print output
    myoutfile.write(output)

