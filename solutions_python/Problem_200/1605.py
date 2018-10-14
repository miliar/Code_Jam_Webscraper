#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python solve.py < input.txt > result.txt

def is_tidy(number):
    str_nbr = str(number)
   # print number
    split_str = list(str_nbr)
    i = len(split_str)-1
    j = 0
    while i > 0:
        #print int(split_str[i])
        if int(split_str[i]) < int(split_str[i-1]):
               sub = ''.join(split_str[i:])
   #            print int(sub)+1
               return int(sub)+1
        i-=1
        j+=1
    return 0

def solve(input):
    number = int(input)
    return_nbr = 1;
    while return_nbr != 0:
        return_nbr = is_tidy(number)
        number-=return_nbr
    return number

if __name__ == "__main__":
    testcases = input()

    for caseNr in xrange(1, testcases+1):
        cipher = raw_input()
        print("Case #%i: %s" % (caseNr, solve(cipher)))

