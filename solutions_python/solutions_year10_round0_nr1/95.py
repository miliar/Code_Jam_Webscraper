#!/usr/bin/python

"""
  Google Code Jam 2010
  Philfifi  --  http://www.pluc.fr
  All rigths reserved
"""

from math import sqrt
from decimal import *
getcontext().prec = 100

import psyco
psyco.full()

_debug = 0


class snapper_chain_c:
    def __init__(self, N):
        self.N = N

        self.power_in_l = [True] + [False] * (N)
        self.state_l = [False] * N
        self.power_out_l = [False] * N

    def snap(self):
        print "----------- before:"
        print "power_in ", [int(i) for i in self.power_in_l]
        print "state     ", [int(i) for i in self.state_l]
        print "power_out  ", [int(i) for i in self.power_out_l]

        for i in range(self.N):
            #Change the state of all powered in
            if self.power_in_l[i]:
                self.state_l[i] = not self.state_l[i]

        for i in range(self.N):
            # calculate power_out
            self.power_out_l[i] = self.power_in_l[i] and self.state_l[i]
            self.power_in_l[i+1] = self.power_out_l[i]

#        print "----------- after:"
#        print "state     ", [int(i) for i in self.state_l]
#        print "power_out  ", [int(i) for i in self.power_out_l]



def solve_case_optim(case_no, N, K):
    if (K +1)%(2**N) == 0:
        return "ON"
    else:
        return "OFF"

def solve_case(case_no, N, K  ):
    print "-------------- New case", case_no


    chain = snapper_chain_c(N)
    for _ in range(K):
        chain.snap()

    if chain.power_out_l[-1]:
        return "ON"
    else:
        return "OFF"



def main(argv):

    f_out_name = argv[1].split(".")[0] + ".out"
    f_out = open(f_out_name, "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        N, K = [int(item) for item in fd.readline().split()]


        # Have read all stuff for this case:
        f_out.write( "Case #%d: %s\n" % (case_no,
                                         solve_case_optim(case_no, N, K)
                                         )
                     )
        f_out.flush()

    f_out.close()

    for line in open(f_out_name):
        print line,



import sys
if __name__ == "__main__":
    main(sys.argv)
