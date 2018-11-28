# -*- coding:utf-8 -*-
'''
Created on 2012/04/14

@author: mutouyutaka
'''


import sys
import itertools

NUMBERS = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

def main() :
    lineNum   = sys.stdin.readline()
    lineNum   = int(lineNum)
    
    for i in range(0, lineNum) :
        line = sys.stdin.readline()
        data = line.strip().split(' ')

        l    = len(data[0])
        A    = int(data[0])
        B    = int(data[1])

        res = 0
        alr = []
#        if l > 1:
##            for num in itertools.permutations(NUMBERS, l):
#            for num in itertools.combinations(NUMBERS, l):
#                is_zero = 0 in num
#                if not is_zero:
#                    num = int(''.join([str(n) for n in num]))
#                if is_zero or (A <= num and num <= B):
#                    if is_zero:
#                        tex = ''.join([str(n) for n in num])
#                    else:
#                        tex = str(num)
#                    sor = ''.join(sorted(list(tex)))
#                    if sor in alr:
#                        continue
##                    for j in xrange(len(tex) - 1):
##                        cyc = int(tex[j+1:] + tex[:j+1])
#                    for cyc in itertools.permutations(tex, l):
#                        cyc = int(''.join([str(n) for n in cyc]))
#                        if str(cyc) in alr: continue
#                        if cyc != num and A <= cyc and cyc <= B:
#                            if not is_zero:
#                                res += 1
#                                print tex, cyc
#                                alr.add(tex)
#                                alr.add(str(cyc))
#                            if is_zero: tex = cyc
#                            is_zero = False
        for num in xrange(A, B + 1):
            tex = str(num)
            for j in xrange(len(tex) - 1):
                cyc = int(tex[j+1:] + tex[:j+1])
                sor = [int(tex), int(cyc)]
                if sorted(sor) in alr: continue
                if int(tex) != cyc and A <= cyc and cyc <= B:
                    res += 1
                    alr.append(sorted(sor))
#                    print tex, cyc
                
        print "Case #%s: %s" % (i + 1, res)


main()
