###
 # Uian Sol Gorgonio <sol.uian@gmail.com>
 # Apr 12 2013
 # Google Code Jam 2013 - Qualification Round
 # Problem C 
 ##

import math
import time

def isPalindrome(numStr):
    mid = len(numStr) / 2
    for i in xrange(mid):
        if numStr[i] != numStr[i - 1]:
            return False
    return True


def resolve(num):
    if isPalindrome(str(num)):
        square = math.sqrt(num)
        if square == math.trunc(square):
            if isPalindrome(str(math.trunc(square))):
                return True
        return False
    return False
    
def gen_all_fai(limit):
    fair_square = []
    for i in xrange(1, limit + 1):
        if isPalindrome(str(i)):
            square = i ** 2
            if isPalindrome(str(square)):
                fair_square.append(square)
    
    return fair_square


# main
fair_square = gen_all_fai(math.trunc(math.sqrt(1000)))

tc = int(raw_input())
for nTC in xrange(1, tc + 1):
    bot, top = map(long, raw_input().split())

    num_fair_square = 0
    for num in fair_square:
        if num >= bot and num <= top:
            num_fair_square += 1

    print "Case #%d: %d" % (nTC, num_fair_square)
