from sys import *
from math import *

tests = input()
for i in range(1, tests + 1):
    count = 0
    line = raw_input().split()
    paint = int(line[1])
    r = int(line[0])
    p = paint
    if(r > 1):
        tmp=(int(r)-2)*2+1
        newPaint = (tmp + 1)*(tmp + 3)/8
    else:
        newPaint = 0
    m = int(sqrt(8*(p+newPaint) + 1)) - 2
    if(r%2 == 1):
        m = ((m+1)/4)*4 - 1
    else:
        m = ((m+3)/4)*4 - 3

    m1=(m-1)/2
    if(r%2):
        k=(m1+1)/2
    else:
        k=(m1/2)+1
    ans = k - int(r)/2
    print "Case #" + repr(i) + ": " + repr(ans).rstrip("L")

