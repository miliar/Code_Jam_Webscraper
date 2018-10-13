#!/usr/bin/python2

import sys

def main(name):
    f = open(name, 'r')
    o = open("output_large.out", 'w')

    num_cases = int(f.readline())
    initial_rate = 2.0

    for i in range(num_cases):
        a = f.readline().split()

        cost_farm = float(a[0])
        farm_rate = float(a[1])
        win_amount = float(a[2])

        print "farms cost", cost_farm
        print "additional farm rate", farm_rate
        print "amount to win", win_amount, "\n"

        #we want to compute the cost of getting j number of farms 
        rates = [initial_rate]
        times_to_win = [win_amount / initial_rate]
        times_to_farm = []
        #we keep on computing costs until it is more expensive to get an additional cookie farm.
        while True:
            #try to get a new farm
            if len(times_to_farm) == 0:
                times_to_farm.append( cost_farm / rates[-1])
            else:
                times_to_farm.append( times_to_farm[-1] + cost_farm /rates[-1])
            #update rates
            rates.append(rates[-1] + farm_rate)

            times_to_win.append(times_to_farm[-1] + win_amount / rates[-1])
            print times_to_win[-1], "Here is latest time to win"

            #if more expensive to try to get a new farm
            if times_to_win[-1] > times_to_win[-2]:
                break       #sorry for the awful use of breaks.





        o.write("Case #" + str(i + 1) + ": " + str(times_to_win[-2]) + "\n")

    o.close()

main(sys.argv[-1])
