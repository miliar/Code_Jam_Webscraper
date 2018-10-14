import sys
import math

def isPalinddrome(n):
    if len(n) == 0:
        return True
    elif n[0] != n[len(n) - 1]:
        return False
    return isPalinddrome(n[1:len(n)-1])

def count_squares(a, b):
    count = 0
    for i in range(a, b+1):
        anum = math.sqrt(i)
        if anum.is_integer() and isPalinddrome(str(i)) and isPalinddrome(str(int(anum))):
            count += 1
    return count

if __name__ == '__main__':
    f = open(sys.argv[1], 'r')
    cases = int(f.readline())
    for j in xrange(cases):
        a, b = f.readline().split(' ')
        a = int(a)
        b = int(b)
        print 'Case #%d: %d' % (j+1, count_squares(a, b))
