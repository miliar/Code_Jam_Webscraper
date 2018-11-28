import sys
import numpy as np
import random
import heapq
from collections import defaultdict

def solve_case_stupid(N, K):
    spaces = [-N]
    for i in range(K):
        max_space = -heapq.heappop(spaces)
        #print max_space
        if max_space == 0:
            print >>sys.stderr, "ERROR!!"
            return -1
        new_max = max_space/2
        new_min = (max_space-1)/2
        assert new_max+new_min+1==max_space
        heapq.heappush(spaces, -new_max)
        heapq.heappush(spaces, -new_min)
    return "%d %d"%(new_max, new_min)

def main_test():
    while True:
        test_num = random.randrange(1,10**6)
        test_K = random.randrange(1,test_num)
        print "Testing %d %d:"%(test_num, test_K)
        smart = solve_case(test_num, test_K)
        print "Smart:", smart
        stupid = solve_case_stupid(test_num, test_K)
        print "Stupid:", stupid
        if stupid != smart:
            print "Failed!"
            print "Stupid:", stupid
            print "Smart:", smart
            return
        print "Success!"

def solve_case(N, K):
    spaces = defaultdict(int) 
    spaces[N] = 1
    max_keys = 1
    i = K
    while i > 0:
        max_space = max(spaces.keys())
        if max_space == 0:
            print >>sys.stderr, "ERROR!!"
            return -1
        num_max_space = spaces.pop(max_space)
        i -= num_max_space
        new_max = max_space/2
        new_min = (max_space-1)/2
        spaces[new_max] += num_max_space 
        spaces[new_min] += num_max_space
    return "%d %d"%(new_max, new_min)

def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    for case_num, line in enumerate(lines[1:]):
        N,K = [int(i) for i in line.split(" ")]
        ans = solve_case(N, K)
        #ans = solve_case_stupid(N, K)
        print "Case #%d:"%(case_num+1), ans

if __name__ == "__main__":
    main()
    #main_test()