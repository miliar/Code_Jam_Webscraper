#!/usr/bin/python


ntests = int(raw_input())

for test in range(ntests):
    n = list(raw_input())

    n = [ int(x) for x in n ]
    v = [ 0 for x in n ]

    lastp = 0
    mx = n[0]
    for p in range(len(n)):
        if mx > n[p]:
            v[lastp] -= 1
            for i in range(p, len(n)):
                v[i] = 9

            for i in range(lastp, 0, -1):
                if v[i] < v[i-1]:
                    v[i] = 9
                    v[i-1] -= 1
                else:
                    break
            break
                
        else:
            v[p] = n[p]
            mx = n[p]
            
            if v[p] != 0:
                lastp = p

    v = [ str(x) for x in v ]
    print ("Case #"+str(test+1)+":"), int("".join(v))
    
