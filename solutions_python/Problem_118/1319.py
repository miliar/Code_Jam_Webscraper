from sys import stdin, stdout
from math import sqrt
from bisect import bisect_left, bisect_right

fair_n_square = set([0,1,4,9])

def isPalindrome(s):
    for i in range(len(s)/2):
        if s[i] is not s[len(s)-1-i]:
            return False
    return True

def preCompute(n):
    for i in range(2,n):
        if i&1:
            for middle in range(0,10):
                for side in range(1,10**(n/2)):
                    number = str(side)[::-1]+str(middle)+str(side)
                    sqnum = int(number)*int(number)
                    snum = str(sqnum)
                    if isPalindrome(snum):
                        fair_n_square.add(sqnum)
        else:
            for side in range(1,10**(n/2)):
                number = str(side)[::-1]+str(side)
                sqnum = int(number)*int(number)
                snum = str(sqnum)
                if isPalindrome(snum):
                    fair_n_square.add(sqnum)
                    
    return sorted(fair_n_square)

            

def solve(l):
    a,b = (int(s) for s in stdin.readline().split())
    return bisect_right(l,b)-bisect_left(l,a)

def main():
    l = preCompute(8)
    testcases = int(stdin.readline())
    for testcase in range(1,testcases+1):
        result = solve(l)
        fstring = "Case #%d: %s" % (testcase,result)
        print fstring

if __name__ == "__main__":
    main()
