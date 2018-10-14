
from math import log 


T = raw_input()
T = int(T)

for i in range(T):
    line = raw_input()
    N, K = line.split()
    N = int(N)
    K = int(K)

    tree = [[N]]
    total = 1
    while total < K:
        cur_level = tree[-1]
        next_level = []
        for j in cur_level:
            if j % 2 == 0:
                next_level.append(j / 2 - 1)
                next_level.append(j / 2)
            else:
                next_level.append(j / 2)
                next_level.append(j / 2)
            total += 2
        tree.append(next_level)
    #print(tree)

    r = K - 2**(int(log(K, 2)))
    sorted_last_level = sorted(tree[-1], reverse=True)
    x = sorted_last_level[r]
    if x % 2 == 0:
        a = x / 2
        b = x / 2 - 1
    else:
        a = x / 2
        b = x / 2

    print("Case #%d: %d %d" % (i+1, a, b))

