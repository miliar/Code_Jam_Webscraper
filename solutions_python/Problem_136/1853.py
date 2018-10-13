#!/usr/bin/env python

problem = 'B-large'

fin = open(problem + '.in')
fout = open(problem + '.out', 'w')

def read_floats():
    return [float(x) for x in fin.readline().strip().split()]

T = int(fin.readline())

for caseno in range(T):
    C, F, X = read_floats()

    total_time = 0
    total_farms = 0
    while (X / (2 + F * total_farms) >
           C / (2 + F * total_farms) +
           X / (2 + F * (total_farms + 1)) ):

        # time to buy a farm
        total_time += C / (2 + F * total_farms)
        total_farms += 1

    # time to make the cookies
    total_time += X / (2 + F * total_farms)
    fout.write("Case #%d: %.7f\n" % (caseno+1, total_time))

fout.close()

