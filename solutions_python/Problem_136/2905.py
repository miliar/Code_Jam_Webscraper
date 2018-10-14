#!/usr/bin/env python

import sys

def main () :
    inp_f = open(sys.argv[1])
    ncases = int(inp_f.readline().strip())

    for icase in range(ncases) :
        c, f, x = [float(fl) for fl in inp_f.readline().split()]

        nfarms = 0
        build_time = 0.0
        cookies_per_second = 2.0
        solution = x / 2.0
        last_solution = x
        while (solution < last_solution) :
           nfarms = nfarms + 1
           last_solution = solution

           build_time = build_time + c/cookies_per_second
           cookies_per_second = cookies_per_second + f

           solution = build_time + x / cookies_per_second

        print 'Case #%i:'%(icase+1),
        print '%.7f' % last_solution

main()
