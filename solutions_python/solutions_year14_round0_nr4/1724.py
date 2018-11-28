#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Aviv
#
# Created:     13/04/2014
# Copyright:   (c) Aviv 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def main():
    f = open('input.in', 'r')
    l = f.readlines()
    f.close()

    f = open('output.txt','w')
    num_tests = int(l.pop(0))
    naomi = []
    ken = []

    for ind in range(num_tests):
        count_cheat = 0
        count_no_cheat = 0
        N = int(l.pop(0))
        naomi_t = l.pop(0).split(' ')
        ken_t = l.pop(0).split(' ')

        for i in range(N):
            naomi.append(float(naomi_t[i]))
            ken.append(float(ken_t[i]))
        naomi = sorted(naomi)
        ken = sorted(ken)

        for i in range(N):
            max_naomi = max(naomi)
            max_ken = max(ken)

            if(max_naomi > max_ken):
                count_cheat += 1
                min_ken = ken.pop(0)
                remove = naomi[0]
                pos = 1
                while (remove < min_ken):
                    remove = naomi[pos]
                    pos += 1
                naomi.pop(pos-1)
            else:
                naomi.pop(0)
                ken.pop(N-i-1)

        for i in range(N):
            naomi.append(float(naomi_t[i]))
            ken.append(float(ken_t[i]))
        naomi = sorted(naomi)
        ken = sorted(ken)

        for index in range(N):
            max_naomi = max(naomi)
            max_ken = max(ken)

            naomi.pop(N-index-1)
            if(max_naomi > max_ken):
                count_no_cheat+=1
                ken.pop(0)

            else:
                ken.pop(N-index-1)


        f.write("Case #{}: {} {}\n".format(ind+1,count_cheat,count_no_cheat))

    f.close()



main()



