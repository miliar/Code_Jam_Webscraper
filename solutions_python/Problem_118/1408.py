import sys;
import math;
import operator;
import collections;

class _:
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return ""
    pass

def isPalindrome(num):
    vnum = list( "%d"%num)
    if vnum == list( reversed(vnum) ):
        return True
    else:
        return False

if __name__ == "__main__":
    n_cases = int(sys.stdin.readline())

    for _i in range(n_cases):
        # Reading...
        result = 0
        A, B = [int(x) for x in sys.stdin.readline().split()]

        # Solving...
        for num in xrange(35): #good enought for B<=1000
            if isPalindrome(num):
                fairSquare =  num*num
                if isPalindrome(fairSquare) and A<=fairSquare and fairSquare<=B:
                    result = result+1

        # printing...
        sys.stderr.write("Case #%s: %s Done!\n"%(_i+1, result))
        print "Case #%s: %s"%(_i+1, result)

