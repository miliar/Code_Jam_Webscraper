#!/usr/bin/python
n = 2 
k = 3 

def solve(n, k):
    """docstring for solve"""
    on = (2 ** n) - 1
    nk = k % (2 ** n)
    if nk == on:
        return "ON" 
    else:
        return "OFF" 


def main():
    """docstring for main"""
    input = open("problem")
    ilines = [l.strip() for l in input.readlines()]
    num_tests = int(ilines[0], 0)
    line_num = 1
    for test in xrange(num_tests):
        line = ilines[line_num]
        line_num = line_num + 1
        (n, k) = [int(x, 0) for x in line.split()]
        print "Case #%d: %s" % (test + 1, solve(n, k))

if __name__ == '__main__':
    main()        

