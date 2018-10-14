import sys

gabriel = [(3, 2, 3), (3, 3, 3), (3, 3, 4), (4, 3, 4), (4, 4, 4)]

t = int(sys.stdin.readline())
for i in range(1, t+1):           
    x, r, c = [int(x) for x in sys.stdin.readline().split()]
    if r > c: r, c = c, r
    print("Case #" + str(i) + ": ", end="")
    if x == 2:
        if r % 2 == 0 or c % 2 == 0: print("GABRIEL")
        else: print("RICHARD")
    else:
        if x == 1 or (x, r, c) in gabriel: print("GABRIEL")
        else: print("RICHARD")