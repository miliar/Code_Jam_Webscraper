#!/usr/bin/python

import math
def isPalindrome(n):
    """
    Tell whether a number palindrome
    """
    n_str = str(n)
    # Get rid of 0 in reverse
    n_reverse = n_str[::-1]
    return n_str == n_reverse

def isSquare(n):
    """
    Tell whether a number square
    """
    root = int(math.sqrt(n))
    return root * root == n

if __name__ == "__main__":
    iter = int(raw_input())

    for i in range(iter):
        count = 0
        inline = raw_input()
        num1, num2 = inline.split(' ')
        num1 = int(num1)
        num2 = int(num2)

        # Get integral of root
        root1 = int(math.floor(math.sqrt(num1)))
        root2 = int(math.floor(math.sqrt(num2))) + 1
        # print "%d %d" %(root1, root2)

        for j in range(root1, root2 + 1):
            squa_j = j * j
            if not isPalindrome(j):
                continue
            if squa_j < num1 or squa_j > num2:
                continue
            else:
                if isPalindrome(squa_j):
                    #print "%d" %(squa_j)
                    count += 1
        print "Case #%d: %d" %(i + 1, count)
