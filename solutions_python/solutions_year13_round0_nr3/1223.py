#! /usr/bin/env python
import math

def main():
    numCases = int(raw_input())
    intervals = []

    for case in xrange(numCases):
        intervals.append([int(num) for num in raw_input().split()])

    caseNum = 0
    for interval in intervals:
        caseNum += 1
        squareFair = 0
        for i in xrange(interval[0],interval[1]+1):
            if is_palindrome(i):
                if is_square(i):
                    if is_palindrome(int(math.sqrt(i))):
                        squareFair += 1
        print "Case #" + str(caseNum) + ": " + str(squareFair)


def is_palindrome(s):
    s = str(s)
    return len(s) < 2 or s[0] == s[-1] and is_palindrome(s[1:-1])

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer:
        return True
    else:
        return False

if __name__=="__main__":
    main()