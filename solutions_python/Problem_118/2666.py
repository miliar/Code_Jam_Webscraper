import sys
from math import sqrt, ceil, modf, floor

def is_palindrome(num):
    snum = str(num)
    lsnum = len(snum)
    if lsnum is 1:
        return 1
    first = snum[0:lsnum/2]
    last = snum[lsnum-1:lsnum-lsnum/2-1:-1]
    
    return first == last

def solve(low, high):
    low_sqrt = int(ceil(sqrt(low)))
    high_sqrt = int(floor(sqrt(high))) + 1
    return sum((is_palindrome(i) and is_palindrome(i**2) for i in xrange(low_sqrt,high_sqrt)))

def main(args):
    test_filename = args[1]
    with open(test_filename) as test_file:
        num_cases =  int(test_file.readline().strip())
        
        for i in xrange(1,num_cases+1):
            case = map(int,test_file.readline().strip().split())
            num_found = solve(*case)
            print "Case #{0}: {1}".format(i,num_found)
            

if __name__ == "__main__":
    main(sys.argv)
