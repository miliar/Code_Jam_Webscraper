#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Jiří Setnička
#
# Created:     13.04.2013
# Copyright:   (c) Jiří Setnička 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def reverse(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n = n // 10
    return rev

def main():
    vstup = open('C_fair_and_square.in', 'r');
    vystup = open('C_fair_and_square.out', 'w');
    [T] = map(int, vstup.readline().split())
    for i in range(1, T+1):
        cases = 0
        [od, do] = map(int, vstup.readline().split());
        for j in range(int(math.ceil(math.sqrt(od))), int(math.floor(math.sqrt(do)))+1):
            if reverse(j)==j:
                power=j*j;
                if(reverse(power)==power and power>=od and power<=do):
                    cases+=1
                    #print power
        vystup.write("Case #"+str(i)+": "+str(cases)+"\n")
    pass

if __name__ == '__main__':
    main()
