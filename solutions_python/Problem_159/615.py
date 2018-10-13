from __future__ import division
from itertools import combinations
from sys import argv

def method1(v):
    sol = 0
    for i in xrange(0, len(v)-1):
        # print v[i]
        mush = v[i] - v[i+1]
        if mush > 0: sol += mush
    return sol

def method2(v):
    sub_list = []
    for i in xrange(0, len(v) -1 ):
        sub_list.append(v[i+1] - v[i])
    # print sub_list
    smallest = min(sub_list)
    if smallest >= 0: return 0
    # sol = abs(smallest)
    sol = 0
    for i in xrange(0, len(v) -1):
        sol += min(abs(smallest), abs(v[i]))
    return sol



def solve(N, v):

    return False 
    

def main():
    filename = 'input.in'
    if len(argv) > 1:
        filename = argv[1]

    with open(filename) as f:
        T = int( f.readline() )
        case_count = 0
        for i in xrange(T):
            case_count += 1
            N = int(f.readline().rstrip('\n'))
            v = map(int, f.readline().rstrip('\n').split(' '))
            
            # ans = solve(N, v)
            
            print "Case #" + str(case_count) + ": " + str(method1(v)) +  " " + str(method2(v))
            
    
main()


