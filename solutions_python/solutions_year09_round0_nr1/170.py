'''
Created on Sep 3, 2009

@author: gatanov
'''
import re
import sys

if __name__ == '__main__':
    [L,D,N] = [int(x) for x in sys.stdin.readline().split()]
    words = range(D)
    for i in range(D):
        words[i] = sys.stdin.readline()
    for case in range(1,N+1):
        pattern = sys.stdin.readline()[:-1].replace("(","[").replace(")","]")
        prog = re.compile(pattern)
        count = 0
        for word in words:
            if (prog.match(word)): count += 1
        print "Case #%d: %d" % (case,count)