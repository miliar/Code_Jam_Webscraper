import sys
import time

T = int(sys.stdin.readline())

def isPaindrome(num):
    """
    >>> isPaindrome('6')
    True
    >>> isPaindrome('9')
    True
    >>> isPaindrome('121')
    True
    """
    if isinstance(num, int):
        num = str(num)
    if len(num) <= 1:
        return True
    if num[0] == num[-1]:
        return isPaindrome(num[1:-1])
    else:
        return False

def isDividerPaindrome(num):
    m = int(num**.5)
    return isPaindrome(m)

def isSquare(num):
    m = int(num**.5)
    return True if abs(m*m - num) < 1e-6 else False

def _test():
    import doctest
    doctest.testmod()

def solve(start, end):
    return len(
            filter(isDividerPaindrome,
                filter(isPaindrome,
                    filter(isSquare, range(start, end+1))
                    )
                )
            )

if __name__ == "__main__":
    #starttime = time.clock()
    for i in xrange(T):
        start, end = [int(x) for x in sys.stdin.readline().rstrip().split()]
        print "Case #{0}: {1}".format(i+1, solve(start, end))
    #endtime = time.clock()
    #print endtime - starttime
