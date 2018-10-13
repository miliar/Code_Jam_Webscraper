'''
Created on April 26, 2013

@author: Anand
'''

import sys

sys.stdin = open('../ABullseye.in')
sys.stdout = open('../ABullseye.out', 'w')

def main():
    T = int(raw_input())
    for testcase in xrange(1, T + 1):
        r, t = (int(x) for x in raw_input().split())
        answer = (0.25) * (-3 - 2 * r + (1 - 4 * r + 4 * r ** 2 + 8 * t) ** 0.5)
        answer = int(answer) + 1
        print "Case #%d: %d" % (testcase, answer)


main()
