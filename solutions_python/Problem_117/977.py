#!/usr/bin/python


import sys
from operator import itemgetter


def check_lawn(rows, n, m):
    """
    n rows
    m columns
    """
    for i in xrange(n):
        for j in xrange(m):
            if rows[i][j] < max(rows[i]) and rows[i][j] < max(map(itemgetter(j), rows)):
                return "NO"
    return "YES"


def main():
    fin_file = sys.argv[1]
    
    with open(fin_file, 'r') as fin:
        T = int(fin.readline().strip())
        
        for t in xrange(T):
            n, m = map(int, fin.readline().strip().split(" "))
            
            rows = []
            
            for _ in xrange(n):
                rows.append(map(int, fin.readline().strip().split(" ")))
            
            print "Case #%d: %s" % ((t + 1), check_lawn(rows, n, m))

        
if __name__ == '__main__':
    main()
    