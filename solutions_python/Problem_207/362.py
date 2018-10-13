#! /usr/bin/env python
cases = int(raw_input())
for case in range(0, cases):
    args = raw_input().split(' ')
    n = int(args[0])
    del args[0]
    u = []
    for i in args:
        u.append(int(i))
    s = []
    c = [[1,0,0],
        [1,0,1],
        [0,0,1],
        [0,1,1],
        [0,1,0],
        [1,1,0]]
    letters = ['R','O','Y','G','B','V']
    h = []
    s = []
    first = -1
    last = -1
    for i in range(0, 6):
        if u[i] != 0:
            h = c[i]
            s.append(letters[i])
            u[i] -= 1
            first = i
            break;

    possible = True
    for i in range(0, n-1):
        f = 0
        b = -1
        for p in range(0, 6):
            j = c[p] 
            match = True
            for i in range(0, 3):
                if h[i] == j[i] and h[i] == 1:
                    match = False
                    break
            if match and u[p] > 0:
                if sum(j) > f:
                    f = sum(j)
                    b = p
                if sum(j) == f:
                    if u[b] < u[p]:
                        b = p
        #print b
        #print f
        if b != -1:
            last = b
            s.append(letters[b])
            h = c[b]
            u[b] -= 1
        else:
            possible = False
            break

    if possible:
       x = c[first] 
       y = c[last]
       for i in range(0, 3):
        if x[i] == y[i] and x[i] == 1:
            possible = False
    if possible:
        print("Case #{}: {}".format(case + 1, ''.join(s)))
    else:
        print("Case #{}: {}".format(case + 1, "IMPOSSIBLE"))
