import numpy as np

t = int(raw_input())
for i in range(1, t+1):
    count = 0
    lst = []
    x, l = raw_input().split()
    for v in x:
        if v == '-':
            lst.append(False)
        else:
            lst.append(True)
    for n in range(len(lst)-int(l)+1):
        if lst[n] is False:
            lst[n:n+int(l)] = [not a for a in lst[n:n+int(l)]]
            count += 1
    if False in lst:
        print "Case #{}: {}".format(i, "IMPOSSIBLE")
    else:
        print "Case #{}: {}".format(i, count)
