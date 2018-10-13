import math


f = open('input', 'r')
g = open('output', 'w')
T = int(f.readline())
for x in range(T):
    (N, K) = tuple([int(i) for i in f.readline().split(" ")])
    stack = [N]
    for i in range(1, K+1, 1):
        m = max(stack)
        l = int(m / 2)
        if m % 2 == 0:
            r = int(m / 2) - 1
        else:
            r = int(m / 2)
        stack.append(l)
        stack.append(r)
        stack.remove(m)
        y = l
        z = r
    g.write("Case #{0}: {1} {2}\n".format(x+1, y, z))
    #print("Case #{0}: {1} {2}\n".format(x+1, y, z))