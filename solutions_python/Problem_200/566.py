import sys
import numpy as np
import random

def test_tidy(nums):
    return np.all(nums[1:] >= nums[:-1])

def solve_case_stupid(N):
    n = int(N)
    for i in range(n,0,-1):
        if test_tidy(np.array([int(j) for j in str(i)])):
            return str(i)

def main_test():
    while True:
        test_num = random.randrange(1,10**6)
        print "Testing %d:"%(test_num)
        smart = solve_case(str(test_num))
        print "Smart:", smart
        stupid = solve_case_stupid(str(test_num))
        print "Stupid:", stupid
        if stupid != smart:
            print "Failed!"
            print "Stupid:", stupid
            print "Smart:", smart
            return
        print "Success!"

def solve_case(N):
    nums = np.array([int(n) for n in N])
    if test_tidy(nums):
        return N
    for i in range(len(nums)-1, -1, -1):
        if not test_tidy(nums[:i]):
            continue
        if (i==0) or (nums[i]-1 >= nums[i-1]):
            ans  = N[:i]
            ans += str(nums[i]-1)
            ans += '9'*(len(N)-i-1)
            return ans.lstrip('0')
    return "ERROR"
    print >>sys.stderr, "This shouldn't happen!!!"

def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    for case_num, line in enumerate(lines[1:]):
        N = line
        ans = solve_case(N)
        #ans = solve_case_stupid(N)
        print "Case #%d:"%(case_num+1), ans

if __name__ == "__main__":
    main()
    #main_test()