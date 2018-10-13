#!/usr/bin/python

import sys
from pprint import pprint

def solve(N):
    digit_n = len(str(N))
    #print digit_n

    str_n = str(N)
    #print str_n
    str_ans = ""
    Tidy = True
    for i in xrange(digit_n - 1):
        #print str_n[i]
        if int(str_n[i]) > int(str_n[i+1]):
            Tidy = False
            j = i
            flag = False
            while j >= 1:
                #print "j:" + str(j)
                if int(str_n[j-1]) < int(str_n[j]):
                    str_ans = str_n[0:j]
                    str_ans += str(int(str_n[j]) - 1)
                    str_ans += "9" * (digit_n - 1 - j)
                    flag = True
                    break
                else:
                  j -= 1
            if flag == False:
                str_ans = str(int(str_n[0]) - 1) +  "9" * (digit_n - 1)
                break
    if Tidy:
        str_ans = str_n
    #print str_ans
    return int(str_ans)

if __name__ == '__main__':

    case_N = int(sys.stdin.readline().strip())
    #pprint(case_N)
    for n in xrange(case_N):
        N = int(sys.stdin.readline().strip())
        tidy_N = solve(N)
        print 'Case #' + str(n+1) + ': ' + str(tidy_N)
