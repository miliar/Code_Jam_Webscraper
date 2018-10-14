#!/usr/bin/env python
# Edward Lau
# 20150410





###############
## VARIABLES ##
###############
IN_FILE="./A-large.in"
OUT_FILE="./A-large.out"
CASES = list()
N_C=0
i_C=0
DEBUG = False
#DEBUG = True





##################
## READ IN FILE ##
##################
with open(IN_FILE, 'r') as f_in:
    ####################
    ## WRITE OUT FILE ##
    ####################
    with open(OUT_FILE, 'w') as f_out:

        N_C = int(f_in.readline())

        ##############
        ## DO STUFF ##
        ##############
        while i_C < N_C:
            i_C += 1
            solution = 0

            L = f_in.readline().split()
            if DEBUG:
                print L

            c = list()
            c.append(i_C)
            c.append(L[0])
            c.append(L[1])

            total = 0
            s_level = 0
            for s in c[2]:
                if s_level == 0:
                    total += int(s)
                else:
                    if total < s_level:
                        #solution += (s_level-total)
                        #total += solution
                        solution += 1
                        total += 1
                        if DEBUG:
                            print "{} {}".format(solution, total)
                    if DEBUG:
                        print s_level
                    total += int(s)
                s_level += 1
#            solution = c[2].count('0')
            c.append(solution)

            if DEBUG:
                print c

            CASES.append(c)

            f_out.write("Case #{}: {}\n".format(i_C, solution))

