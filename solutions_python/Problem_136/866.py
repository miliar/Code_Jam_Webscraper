#!/usr/bin/env python
import sys

def print_result(tc_number, res):
    print "Case #{0}:".format(tc_number), res

def main():
    data = sys.stdin
    N = int(data.readline())
    
    test_case = 1       
    while test_case <= N:
        C, F, X = map(float, data.readline().split())
        # print C, F, X
        time = 0
        Rate = 2

        while True:
            if float(X/Rate) < float(X/(Rate + F) + (C/Rate)):
                time += float(X/Rate)
                break
            else:
                time += float(C/Rate)
                Rate = Rate + F
        print_result(test_case, '%.7f' % time)        
        test_case += 1
    
if __name__ == '__main__':
    main()