#!/usr/bin/env python

import sys


def get():
    number = int(sys.stdin.readline())
    for i in range(1, number):
        sys.stdin.readline()
    #endfor
    row = (int(one) for one in sys.stdin.readline().split(" "))
    for i in range(number, 4):
        sys.stdin.readline()
    #endfor
    return list(row)
#enddef
def solve():
    f = get()
    s = get()
    i = list(set(f) & set(s))
    if len(i) > 1:
        return "Bad magician!"
    if len(i) == 0:
        return "Volunteer cheated!"
        
    return i[0]
#enddef

def main():
	T = int(sys.stdin.readline())
	for caseNumber in xrange(1, T+1):
	    print "Case #%d: %s" % (caseNumber, solve())
	#endfor
#enddef

if __name__ == '__main__':
	main()
#endif


