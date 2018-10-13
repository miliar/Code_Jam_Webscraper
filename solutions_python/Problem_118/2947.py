# Google-Code-Jam
# C. fair and square

import math
def isPalindrome(num) :
    numstr = str(num)
    return numstr == numstr[: : -1]

no_of_tc = int(raw_input())
for tc in range(no_of_tc) :
    line = raw_input()
    left = int(line.split(' ')[0])
    right = int(line.split(' ')[1])
    no_of_fsqrs = 0
    if math.sqrt(left) % 1 == 0 : leftc = int(math.sqrt(left))
    else : leftc = int(math.sqrt(left)) + 1
    rightc = int(math.sqrt(right)) + 1
    for num in range(leftc, rightc) :
        if isPalindrome(num) and isPalindrome(num * num) : no_of_fsqrs += 1
    print 'Case #%d: %d' %(tc + 1, no_of_fsqrs)

