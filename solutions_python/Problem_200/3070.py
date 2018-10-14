#!/usr/bin/env python

"""
Developed by Jormar Arellano <jormar.arellano@gmail.com>

Google Code Jam 2017

Problem TODO - TODO

Notes:
"""

import sys
import math
import operator
import collections


class _:

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return ""
    pass


# contadoParaMemory = {}
#
#
# def contadoPara(numDigito, digito):
#     if (numDigito, digito) in contadoParaMemory:
#         total = contadoParaMemory[(numDigito, digito)]
#     else:
#         total = 0
#         if numDigito == 1:
#             total = 9 - digito + 1
#         else:
#             for i in xrange(numDigito-1, 0, -1):
#                 for j in xrange(digito, 10):
#                     total += contadoPara(i, j)
#         contadoParaMemory[(numDigito, digito)] = total
#         print (numDigito, digito), total
#     return total

def isTidy(number):
    strNumber = str(number)
    for i in xrange(0, len(strNumber)-1):
        if strNumber[i] > strNumber[i+1]:
            return False
    return True


if __name__ == "__main__":
    n_cases = int(raw_input())  # read a line with a single integer

    for _i in xrange(n_cases):
        # Reading...
        N = [int(s)for s in raw_input().split(" ")]
        N = N[0]
        lenN = len(str(N))
        result = N

        # Solving...
        for i in xrange(1, lenN+1):
            if isTidy(result):
                break

            # Restamos todo lo necesario para saltar al posible anterior Tidy
            digit = result % 10**i / 10**(i-1)
            result -= (digit+1)*(10**(i-1))

        # printing...
        sys.stderr.write("Case #%s: %s Done!\n" % (_i + 1, result))
        print "Case #%s: %s" % (_i + 1, result)
