#!/usr/bin/python

# Drew Gassaway
# GCJ 2014 Qualification B

import sys

BASERATE = 2.0

# generic Google Code Jam function wrapped for
# basic "T" test cases input schema

def jam (infile, outfile):

    with open(infile, "r") as fp:

        out = open(outfile, "w")
        numcases = int(fp.readline().strip())

        for casenum in range(numcases):

            #############     Problem Logic Here

            specs = fp.readline().strip().split(' ')
            C = float(specs[0])
            F = float(specs[1])
            X = float(specs[2])

            # reach X optimally. output time in seconds to 7 decimal places
            # Every time you have C cookies, can increase rate by F.
            # strategy:
            #   calculate cost at current rate of reaching X (cost in sec)
            #   calculate cost2 to accumulate C, and reach X at rate + F
            #   if cost2 < cost, current rate = rate + F. set other vars as if we just reached that farm level.
            #   if cost2 >= cost, done, return cost

            optimal_cost = 0.0
            current_rate = BASERATE
            run_time = 0.0

            while(True):

                # calc once vars
                next_rate = current_rate + F
                addl_time = C / current_rate

                current_cost = X / current_rate
                next_cost = addl_time + X / next_rate

                if current_cost <= next_cost:
                    optimal_cost = run_time + current_cost
                    break

                else:
                    current_rate = next_rate
                    run_time += addl_time

            result = str("{0:.7f}".format(optimal_cost))

            # debug parse
            #print "C: " + str(C) + " F: " + str(F) + " X: " + str(X)

            #############     Case output here as 'result'

            out.write("Case #" + str(casenum + 1) + ": " + result + '\n')

        out.close()


### generic main

if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " <input_file> <output_file>"
    exit(1)

jam(sys.argv[1], sys.argv[2])

