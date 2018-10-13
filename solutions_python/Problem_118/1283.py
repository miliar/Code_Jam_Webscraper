#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math

def main():
    pass

if __name__ == '__main__':
    main()
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      tim
#
# Created:     13/04/2013
# Copyright:   (c) tim 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------



def palindrome(num):
    str = '%d' % num
    n = len(str)
    for i in range(0, n/2):
        if str[i] != str [n - 1 - i]:
            return False
    return True

def main():
    pass

if __name__ == '__main__':
    main()

result = []
T = 0

with open('C-small-attempt0.IN') as f:
    T = int(f.readline())

    for t in range(0, T):
        arr = f.readline().split(' ')
        A = int(arr[0])
        B = int(arr[1])
        a = int( math.sqrt(A) )
        if a*a < A:
            a += 1
        b = int( math.sqrt(B) )
        if b*b > B:
            b = b-1

        cnt = 0
        for i in range(a, b+1):
            if palindrome(i) and palindrome( i * i):
                cnt += 1

        result.append(cnt)


###############
print result
with open('C-small-attempt0.OUT', 'w') as f:
    for  i in range(0, T):
        f.write("Case #%d: %s\n" % (i+1, result[i]) )