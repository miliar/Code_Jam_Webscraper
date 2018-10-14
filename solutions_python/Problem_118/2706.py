import sys
import math

# take string, tell if palindrome
def ispal(s):
    length = len(s)
    if length==1:
        return True

    for i in range(length/2 + 1):
        if s[i] != s[length-1-i]:
            return False
    return True

# take int
def sqrtwhole(n):
    sq = math.sqrt(n)
    return sq % int(sq) == 0

def case(fd):
    start, end = fd.readline().split(' ')
    start = int(start)
    end = int(end)

    numFS = 0 # fair and square
    for i in range(start,end+1):
        if ispal(str(i)):
            if sqrtwhole(i):
                if ispal(str(int(math.sqrt(i)))):
                    numFS += 1
    
    return str(numFS)

def main():
    fd = sys.stdin
    n = int(fd.readline())
    for i in range(n):
        print 'Case #%d: %s' % (i+1, case(fd))

main()
