import sys

t = int(sys.stdin.readline())

for i in range(t):
    sys.stdout.write("Case #{0}: ".format(str(i + 1)))
    c, f, x = map(float, sys.stdin.readline().split())
    r = 2
    total = 0
    totalTime = 0
    while True:
        eta = (x - total) / r
        dec = (c - total) / r
        beta = x / (r + f) + dec
        if beta < eta:
            totalTime += dec
            total = total + dec * r - c
            r += f
        else:
            totalTime += eta
            break
    sys.stdout.write(str(totalTime))
        
    sys.stdout.write("\n")