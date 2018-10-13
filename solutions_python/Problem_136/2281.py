__author__ = 'parad0x'

from decimal import *

my_file = open("B-large.in","r")
cases = int(my_file.readline())

for i in range(cases):
    data = my_file.readline().rstrip('\n')
    values = data.split(' ')
    c = Decimal(values[0])
    f = Decimal(values[1])
    x = Decimal(values[2])

    min_time = 0
    min_time2 = 0
    counter = 0
    seconds = 0
    seconds2 = 0
    time = 0
    t = 0
    rate = 2
    while counter >= 0:
        min_time2 = seconds + t - time
        if min_time2 < min_time:
            break
        time = c/rate
        seconds += time
        t = x/rate
        min_time = seconds + t - time
        '''print (counter, round(rate),round(time,4),round(seconds,4),round(t,4), round(min_time,4),round(min_time2,4))'''
        if min_time2 < min_time and min_time2 != 0:
            break
        rate = rate + f
        counter += 1

    out = round(min_time2,7)
    if out == 0:
        print ("Case #" + str(i+1) + ": 1.0000000")
    else:
        print ("Case #" + str(i+1) + ":", out)

my_file.close()