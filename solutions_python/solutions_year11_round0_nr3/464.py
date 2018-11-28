"""
Candy Splitting
Code Jam 2011

Credit: Algorithm by Eng! (YRTBS)
"""
import sys
import operator

def split_candies(candies):
    if reduce(operator.xor, candies):
        return "NO"
    else:
        candies.pop(candies.index(min(candies))) # for Pactrick
        return sum(candies)

def main():
    num_tests = int(sys.stdin.readline())
    for t in range(1, num_tests + 1):
        sys.stdin.readline() # ignore number of candies
        candies = [int(x) for x in sys.stdin.readline().split()]
        result = split_candies(candies)
        print "Case #%d: %s" % (t, result)

if __name__ == '__main__':
    main()
