from __future__ import division
from sys import stdin

def is_square(apositiveint):
    if apositiveint == 1:
        return 1
    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen:
            return False
        seen.add(x)
    return x
  
def is_pal(number):
    number = str(number)
    rev = number[::-1]
    if(number == rev):
        return True
    return False

T = stdin.readline().strip()
T = int(T)
for t in range(1,T+1):
    line = stdin.readline().strip()
    line = line.split()
    A = int(line[0])
    B = int(line[1])
    result = 0
    for i in range(A,B+1):
        if is_pal(i):
            sqrt = is_square(i)
            if sqrt and is_pal(sqrt):
                result += 1
    print "Case #%d: %d"%(t,result)
    