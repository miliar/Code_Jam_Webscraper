#-------------------------------------------------------------------------------
# Name:        CookieMonster
# Purpose:
#
# Author:      Aviv
#
# Created:     12/04/2014
# Copyright:   (c) Aviv 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
sys.setrecursionlimit(2000)

def CookieMonster(C,F,X,R):
    no_farm=X/R
    farm_one_step=C/R+X/(R+F)
    if (no_farm < farm_one_step):
        return no_farm

    return C/R + CookieMonster(C,F,X,R+F)

def main():
    inp = open('input.in','r')
    tests =inp.readlines()
    inp.close()
    res = []

    num_tests = int(tests.pop(0))
    for ind in range(num_tests):
        data = tests.pop(0).split(' ')
        #print(data)
        time = CookieMonster(float(data[0]),float(data[1]),float(data[2]),2)
        res.append("Case #{}: {}\n".format(ind+1,time))
    output = open('output.txt','w')
    output.writelines(res)


main()