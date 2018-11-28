import math

r = 0

def paint(n):
    x = 2*n - 1
    return 2*(x+r) - 1

num = int(raw_input())

for test in range(num):
    r, t = map(int,raw_input().split())
    circle = 0
    while True:
        req = paint(circle+1)
        if req <= t:
            t -= req
            circle += 1
        else:
            break
    print "Case #%d: %d" % (test+1, circle)
