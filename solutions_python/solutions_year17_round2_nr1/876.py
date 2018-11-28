#import fileinput
#f = fileinput.input()
import sys
t = input()
c = 0
while t:
    c += 1
    t -= 1
    [d,n] = map(int,raw_input().split())
    maxtime = 0
    while n:
        n -= 1
        [k,s] = map(int,raw_input().split())
        time = (d-k)*1.0 / s
        if time > maxtime:
            maxtime = time
    res = '{0:.6f}'.format(d*1.0/maxtime)
    res = "Case #"+str(c)+": "+res
    if c!=0:
        sys.stdout.write("\n")
    sys.stdout.write(res)
